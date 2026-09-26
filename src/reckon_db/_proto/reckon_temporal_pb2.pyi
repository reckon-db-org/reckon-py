from . import reckon_shared_pb2 as _reckon_shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadUntilRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "timestamp", "batch_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    timestamp: int
    batch_size: int
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., timestamp: _Optional[int] = ..., batch_size: _Optional[int] = ...) -> None: ...

class ReadRangeRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "from_timestamp", "to_timestamp", "batch_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TO_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    from_timestamp: int
    to_timestamp: int
    batch_size: int
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., from_timestamp: _Optional[int] = ..., to_timestamp: _Optional[int] = ..., batch_size: _Optional[int] = ...) -> None: ...

class VersionAtRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "timestamp")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    timestamp: int
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ReadUntilResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.RecordedEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]]] = ...) -> None: ...

class ReadRangeResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.RecordedEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]]] = ...) -> None: ...

class VersionAtResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...
