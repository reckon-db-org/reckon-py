import reckon_shared_pb2 as _reckon_shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterSchemaRequest(_message.Message):
    __slots__ = ("store_id", "event_type", "schema")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    event_type: str
    schema: bytes
    def __init__(self, store_id: _Optional[str] = ..., event_type: _Optional[str] = ..., schema: _Optional[bytes] = ...) -> None: ...

class UnregisterSchemaRequest(_message.Message):
    __slots__ = ("store_id", "event_type")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    event_type: str
    def __init__(self, store_id: _Optional[str] = ..., event_type: _Optional[str] = ...) -> None: ...

class GetSchemaRequest(_message.Message):
    __slots__ = ("store_id", "event_type")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    event_type: str
    def __init__(self, store_id: _Optional[str] = ..., event_type: _Optional[str] = ...) -> None: ...

class ListSchemasRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class GetSchemaVersionRequest(_message.Message):
    __slots__ = ("store_id", "event_type")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    event_type: str
    def __init__(self, store_id: _Optional[str] = ..., event_type: _Optional[str] = ...) -> None: ...

class UpcastEventsRequest(_message.Message):
    __slots__ = ("store_id", "events")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.RecordedEvent]
    def __init__(self, store_id: _Optional[str] = ..., events: _Optional[_Iterable[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]]] = ...) -> None: ...

class RegisterSchemaResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UnregisterSchemaResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSchemaResponse(_message.Message):
    __slots__ = ("event_type", "schema", "version")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    schema: bytes
    version: int
    def __init__(self, event_type: _Optional[str] = ..., schema: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class ListSchemasResponse(_message.Message):
    __slots__ = ("schemas",)
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedCompositeFieldContainer[GetSchemaResponse]
    def __init__(self, schemas: _Optional[_Iterable[_Union[GetSchemaResponse, _Mapping]]] = ...) -> None: ...

class GetSchemaVersionResponse(_message.Message):
    __slots__ = ("version",)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int
    def __init__(self, version: _Optional[int] = ...) -> None: ...

class UpcastEventsResponse(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.RecordedEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]]] = ...) -> None: ...
