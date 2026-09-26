"""Streams: append and read events from a single stream."""

import reckon_db
from reckon_db._proto import reckon_streams_pb2 as streams_pb
from reckon_db._proto import reckon_streams_pb2_grpc as streams_grpc

channel = reckon_db.connect("localhost:50051", insecure=True)
stub = streams_grpc.StreamServiceStub(channel)

resp = stub.AppendEvents(streams_pb.AppendEventsRequest(
    store_id="default_store",
    stream_id="users-1",
    expected_version=reckon_db.NoStream,
    events=[streams_pb.ProposedEvent(
        event_type="user_registered_v1",
        data=b'{"name": "Alice"}',
        tags=["email:alice@example.com"],
    )],
))
print(f"appended: version={resp.version} position={resp.position}")

read = stub.ReadStreamForward(streams_pb.ReadStreamRequest(
    store_id="default_store",
    stream_id="users-1",
    start_version=0,
    count=100,
))
for ev in read.events:
    print(f"  {ev.version} {ev.event_type} {ev.tags}")

channel.close()
