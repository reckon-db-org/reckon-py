# reckon-py

Python gRPC client for [ReckonDB](https://github.com/reckon-db-org).

Packages the generated stubs for all ReckonDB services and adds three thin conveniences:
`connect()`, named integer sentinels, and TagFilter helpers for DCB queries.

## Install

```bash
pip install reckon-py
```

The distribution is `reckon-py`; the import package is `reckon_db`:

```python
import reckon_db
```

Requires Python 3.10+, grpcio ≥ 1.81.1, protobuf ≥ 6.33.5 and < 7: the
versions the stubs were generated with, and the oldest they run on. 0.2.0 is the first
release on PyPI.

## Quick start

```python
import reckon_db
from reckon_db._proto import reckon_streams_pb2 as streams_pb
from reckon_db._proto import reckon_streams_pb2_grpc as streams_grpc

channel = reckon_db.connect("localhost:50051", insecure=True)
stub = streams_grpc.StreamServiceStub(channel)

stub.AppendEvents(streams_pb.AppendEventsRequest(
    store_id="default_store",
    stream_id="users-1",
    expected_version=reckon_db.AnyVersion,
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
| `reckon_db._proto.reckon_streams_pb2[_grpc]` | Streams (append, read, watch, indexed reads) |
| `reckon_db._proto.reckon_dcb_pb2[_grpc]` | DCB (cross-aggregate conditional append) |
| `reckon_db._proto.reckon_subscriptions_pb2[_grpc]` | Persistent subscriptions |
| `reckon_db._proto.reckon_snapshots_pb2[_grpc]` | Snapshots |
| `reckon_db._proto.reckon_temporal_pb2[_grpc]` | Temporal reads (read until or between points in time, version at a time) |
| `reckon_db._proto.reckon_schema_pb2[_grpc]` | Schemas (register, list, version, upcast events) |
| `reckon_db._proto.reckon_stores_pb2[_grpc]` | Store discovery |
| `reckon_db._proto.reckon_admin_pb2[_grpc]` | Administration (store and stream stats, scavenge, stream links, catalogue) |
| `reckon_db._proto.reckon_health_pb2[_grpc]` | Health checks |
| `reckon_db._proto.reckon_shared_pb2` | Shared types |

## Sentinels

```python
reckon_db.AnyVersion        # -2  append regardless of current stream version
reckon_db.NoStream          # -1  append only if the stream does not exist
reckon_db.StreamExists      # -4  append only if the stream exists

reckon_db.SEQ_CUTOFF_SAW_NOTHING  # -1  DCB: treat any match as a conflict
```

## DCB TagFilter helpers

```python
import reckon_db
from reckon_db._proto import reckon_dcb_pb2 as dcb_pb
from reckon_db._proto import reckon_dcb_pb2_grpc as dcb_grpc

stub = dcb_grpc.DcbServiceStub(channel)
f = reckon_db.and_(
    reckon_db.event_type("seat_reserved_v1"),
    reckon_db.match_any("seat:FL-42:A3"),
)

ctx = stub.ReadDcbContext(dcb_pb.ReadDcbContextRequest(
    store_id="default_store",
    tag_filter=f,
))
cutoff = ctx.max_seq if ctx.events else reckon_db.SEQ_CUTOFF_SAW_NOTHING

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
channel = reckon_db.connect("localhost:50051", insecure=True)

# System root pool
channel = reckon_db.connect("reckon.example.com:50051")

# Private CA
channel = reckon_db.connect("reckon.example.com:50051", ca_cert="/path/to/ca.pem")

# IP dial with SNI override
channel = reckon_db.connect("10.0.0.5:50051", server_name_override="reckon.example.com")
```

## Regenerating stubs

If you update the proto definitions:

```bash
pip install grpcio-tools
./scripts/gen_proto.sh
```

## License

Apache-2.0
