"""DCB: cross-aggregate conditional append (email uniqueness example)."""

import reckon
from reckon._proto import reckon_dcb_pb2 as dcb_pb
from reckon._proto import reckon_dcb_pb2_grpc as dcb_grpc
from reckon._proto import reckon_streams_pb2 as streams_pb

channel = reckon.connect("localhost:50051", insecure=True)
stub = dcb_grpc.DcbServiceStub(channel)

email = "alice@example.com"
f = reckon.and_(
    reckon.event_type("user_registered_v1"),
    reckon.match_any(f"email:{email}"),
)

for attempt in range(5):
    ctx = stub.ReadDcbContext(dcb_pb.ReadDcbContextRequest(
        store_id="default_store",
        tag_filter=f,
    ))
    if any(e.event_type == "user_registered_v1" for e in ctx.events):
        print("email already taken")
        break

    cutoff = ctx.max_seq if ctx.events else reckon.SEQ_CUTOFF_SAW_NOTHING
    resp = stub.AppendIfNoTagMatches(dcb_pb.AppendIfNoTagMatchesRequest(
        store_id="default_store",
        tag_filter=f,
        seq_cutoff=cutoff,
        events=[streams_pb.ProposedEvent(
            event_type="user_registered_v1",
            data=b'{"name": "Alice"}',
            tags=[f"email:{email}"],
        )],
    ))
    if resp.HasField("committed"):
        print(f"registered: last_seq={resp.committed.last_seq}")
        break
    print(f"conflict on attempt {attempt + 1}, retrying")

channel.close()
