# reckon-py

Python gRPC client for [ReckonDB](https://codeberg.org/reckon-db-org).

Packages the generated stubs for all ReckonDB services and adds three thin conveniences:
`connect()`, named integer sentinels, and TagFilter helpers for DCB queries.

## Install

```bash
pip install reckon-py
```

Requires Python 3.10+, grpcio ≥ 1.60, protobuf ≥ 4.0.

## Quick start

```python
import reckon
from reckon._proto import reckon_streams_pb2 as streams_pb
from reckon._proto import reckon_streams_pb2_grpc as streams_grpc

channel = reckon.connect("localhost:50051", insecure=True)
stub = streams_grpc.StreamServiceStub(channel)

stub.AppendEvents(streams_pb.AppendEventsRequest(
    store_id="default_store",
    stream_id="users-1",
    expected_version=reckon.AnyVersion,
    events=[streams_pb.ProposedEvent(
        event_type="user_registered_v1",
        data=b'{"name": "Alice"}',
        tags=["email:alice@example.com"],
    )],
))
```

## Available proto modules

| Module | Service |
|--------|---------|
| `reckon._proto.reckon_streams_pb2[_grpc]` | Streams (append, read, watch, indexed reads) |
| `reckon._proto.reckon_dcb_pb2[_grpc]` | DCB (cross-aggregate conditional append) |
| `reckon._proto.reckon_subscriptions_pb2[_grpc]` | Persistent subscriptions |
| `reckon._proto.reckon_stores_pb2[_grpc]` | Store discovery |
| `reckon._proto.reckon_health_pb2[_grpc]` | Health checks |
| `reckon._proto.reckon_shared_pb2` | Shared types |

## Sentinels

```python
reckon.AnyVersion        # -2  append regardless of current stream version
reckon.NoStream          # -1  append only if the stream does not exist
reckon.StreamExists      # -4  append only if the stream exists

reckon.SEQ_CUTOFF_SAW_NOTHING  # -1  DCB: treat any match as a conflict
```

## DCB TagFilter helpers

```python
import reckon
from reckon._proto import reckon_dcb_pb2 as dcb_pb
from reckon._proto import reckon_dcb_pb2_grpc as dcb_grpc

stub = dcb_grpc.DcbServiceStub(channel)
f = reckon.and_(
    reckon.event_type("seat_reserved_v1"),
    reckon.match_any("seat:FL-42:A3"),
)

ctx = stub.ReadDcbContext(dcb_pb.ReadDcbContextRequest(
    store_id="default_store",
    tag_filter=f,
))
cutoff = ctx.max_seq if ctx.events else reckon.SEQ_CUTOFF_SAW_NOTHING

resp = stub.AppendIfNoTagMatches(dcb_pb.AppendIfNoTagMatchesRequest(
    store_id="default_store",
    tag_filter=f,
    seq_cutoff=cutoff,
    events=[...],
))
if resp.HasField("committed"):
    print("done", resp.committed.last_seq)
```

All helpers return `reckon_dcb_pb2.TagFilter` objects directly.

| Helper | Proto field |
|--------|-------------|
| `match_any(*tags)` | `TagFilter.match_any` |
| `match_all(*tags)` | `TagFilter.match_all` |
| `event_type(t)` | `TagFilter.event_type_match` |
| `and_(*filters)` | `TagFilter.conjunction` |
| `or_(*filters)` | `TagFilter.disjunction` |

## TLS

```python
# Plaintext (lab / loopback only)
channel = reckon.connect("localhost:50051", insecure=True)

# System root pool
channel = reckon.connect("reckon.example.com:50051")

# Private CA
channel = reckon.connect("reckon.example.com:50051", ca_cert="/path/to/ca.pem")

# IP dial with SNI override
channel = reckon.connect("10.0.0.5:50051", server_name_override="reckon.example.com")
```

## Regenerating stubs

If you update the proto definitions:

```bash
pip install grpcio-tools
./scripts/gen_proto.sh
```

## License

Apache-2.0
