"""ReckonDB Python client.

reckon-py packages the ReckonDB gRPC stubs and adds three things:

1. ``connect()`` — channel factory with TLS options
2. Expected-version sentinels (``AnyVersion``, ``NoStream``, ``StreamExists``)
   and DCB seq sentinel (``SEQ_CUTOFF_SAW_NOTHING``)
3. TagFilter helpers (``match_any``, ``match_all``, ``event_type``, ``and_``, ``or_``)
   that build ``reckon_dcb_pb2.TagFilter`` proto objects

Everything else is the raw generated stubs under ``reckon._proto``.

Usage::

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

DCB decision loop::

    from reckon._proto import reckon_dcb_pb2 as dcb_pb
    from reckon._proto import reckon_dcb_pb2_grpc as dcb_grpc

    stub = dcb_grpc.DcbServiceStub(channel)
    f = reckon.and_(
        reckon.event_type("seat_reserved_v1"),
        reckon.match_any("seat:FL-42:A3"),
    )

    for _ in range(5):
        ctx = stub.ReadDcbContext(dcb_pb.ReadDcbContextRequest(
            store_id="default_store",
            tag_filter=f,
        ))
        cutoff = ctx.max_seq if ctx.events else reckon.SEQ_CUTOFF_SAW_NOTHING

        resp = stub.AppendIfNoTagMatches(dcb_pb.AppendIfNoTagMatchesRequest(
            store_id="default_store",
            tag_filter=f,
            seq_cutoff=cutoff,
            events=[streams_pb.ProposedEvent(
                event_type="seat_reserved_v1",
                data=b'{"booking_id":"b-1"}',
                tags=["seat:FL-42:A3"],
            )],
        ))
        if resp.HasField("committed"):
            break
"""

from __future__ import annotations

import grpc

from reckon._proto import reckon_dcb_pb2 as _dcb

# ──────────────────────────────────────────────
# Expected-version sentinels (streams)
# ──────────────────────────────────────────────

#: Append only if the stream does not exist yet.
NoStream: int = -1
#: No concurrency check — always append.
AnyVersion: int = -2
#: Append only if the stream already exists (at any version).
StreamExists: int = -4

# ──────────────────────────────────────────────
# DCB seq sentinel
# ──────────────────────────────────────────────

#: Pass as seq_cutoff when you have seen no matching events yet.
#: Any matching event in the store will be treated as a conflict.
SEQ_CUTOFF_SAW_NOTHING: int = -1

# ──────────────────────────────────────────────
# TagFilter helpers
# ──────────────────────────────────────────────


def match_any(*tags: str) -> _dcb.TagFilter:
    """Match if the event carries ANY of the given tags."""
    return _dcb.TagFilter(match_any=_dcb.TagList(tags=list(tags)))


def match_all(*tags: str) -> _dcb.TagFilter:
    """Match if the event carries ALL of the given tags."""
    return _dcb.TagFilter(match_all=_dcb.TagList(tags=list(tags)))


def event_type(t: str) -> _dcb.TagFilter:
    """Match if the event's event_type equals t."""
    return _dcb.TagFilter(event_type_match=t)


def and_(*filters: _dcb.TagFilter) -> _dcb.TagFilter:
    """Match if ALL sub-filters match (conjunction)."""
    return _dcb.TagFilter(conjunction=_dcb.FilterList(filters=list(filters)))


def or_(*filters: _dcb.TagFilter) -> _dcb.TagFilter:
    """Match if ANY sub-filter matches (disjunction)."""
    return _dcb.TagFilter(disjunction=_dcb.FilterList(filters=list(filters)))


# ──────────────────────────────────────────────
# Channel factory
# ──────────────────────────────────────────────


def connect(
    endpoint: str,
    *,
    insecure: bool = False,
    ca_cert: str | None = None,
    server_name_override: str | None = None,
) -> grpc.Channel:
    """Open a gRPC channel to a reckon-gateway endpoint.

    endpoint: ``host:port`` (e.g. ``"localhost:50051"``).

    Transport security:
    - Default (no flags): TLS verified against the system root pool.
    - ``insecure=True``: plaintext — lab / loopback only.
    - ``ca_cert``: path to a PEM bundle for private-CA gateways.
    - ``server_name_override``: TLS SNI override (when dialling by IP).

    The returned channel is a standard ``grpc.Channel``. Pass it to any
    stub constructor from ``reckon._proto``::

        channel = reckon.connect("localhost:50051", insecure=True)
        stub = reckon_streams_pb2_grpc.StreamServiceStub(channel)
    """
    if insecure:
        return grpc.insecure_channel(endpoint)

    options: list[tuple[str, str]] = []
    if server_name_override:
        options.append(("grpc.ssl_target_name_override", server_name_override))

    if ca_cert is not None:
        with open(ca_cert, "rb") as f:
            pem = f.read()
        creds = grpc.ssl_channel_credentials(root_certificates=pem)
    else:
        creds = grpc.ssl_channel_credentials()

    return grpc.secure_channel(endpoint, creds, options=options or None)


__all__ = [
    "connect",
    "AnyVersion",
    "NoStream",
    "StreamExists",
    "SEQ_CUTOFF_SAW_NOTHING",
    "match_any",
    "match_all",
    "event_type",
    "and_",
    "or_",
]
