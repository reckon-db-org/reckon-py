import reckon_shared_pb2 as _reckon_shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppendEventsRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "expected_version", "events")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_VERSION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    expected_version: int
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.ProposedEvent]
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., expected_version: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_reckon_shared_pb2.ProposedEvent, _Mapping]]] = ...) -> None: ...

class ReadStreamRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "start_version", "count")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    START_VERSION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    start_version: int
    count: int
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., start_version: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class GetStreamVersionRequest(_message.Message):
    __slots__ = ("store_id", "stream_id")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ...) -> None: ...

class ListStreamsRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class DeleteStreamRequest(_message.Message):
    __slots__ = ("store_id", "stream_id")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ...) -> None: ...

class ReadByEventTypesRequest(_message.Message):
    __slots__ = ("store_id", "event_types", "batch_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    event_types: _containers.RepeatedScalarFieldContainer[str]
    batch_size: int
    def __init__(self, store_id: _Optional[str] = ..., event_types: _Optional[_Iterable[str]] = ..., batch_size: _Optional[int] = ...) -> None: ...

class ReadByTagsRequest(_message.Message):
    __slots__ = ("store_id", "tags", "match", "batch_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    tags: _containers.RepeatedScalarFieldContainer[str]
    match: _reckon_shared_pb2.TagMatch
    batch_size: int
    def __init__(self, store_id: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., match: _Optional[_Union[_reckon_shared_pb2.TagMatch, str]] = ..., batch_size: _Optional[int] = ...) -> None: ...

class ReadByMetadataRequest(_message.Message):
    __slots__ = ("store_id", "key", "value", "batch_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    key: str
    value: str
    batch_size: int
    def __init__(self, store_id: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[str] = ..., batch_size: _Optional[int] = ...) -> None: ...

class ReadAllGlobalRequest(_message.Message):
    __slots__ = ("store_id", "offset", "limit")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    offset: int
    limit: int
    def __init__(self, store_id: _Optional[str] = ..., offset: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class AppendEventsResponse(_message.Message):
    __slots__ = ("version", "position", "count")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    version: int
    position: int
    count: int
    def __init__(self, version: _Optional[int] = ..., position: _Optional[int] = ..., count: _Optional[int] = ...) -> None: ...

class ReadStreamResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.RecordedEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]]] = ...) -> None: ...

class GetStreamVersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class ListStreamsResponse(_message.Message):
    __slots__ = ("stream_ids",)
    STREAM_IDS_FIELD_NUMBER: _ClassVar[int]
    stream_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, stream_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteStreamResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
