from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoreEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORE_EVENT_TYPE_UNSPECIFIED: _ClassVar[StoreEventType]
    STORE_EVENT_TYPE_ANNOUNCED: _ClassVar[StoreEventType]
    STORE_EVENT_TYPE_RETIRED: _ClassVar[StoreEventType]

class StoreMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STORE_MODE_UNSPECIFIED: _ClassVar[StoreMode]
    STORE_MODE_SINGLE: _ClassVar[StoreMode]
    STORE_MODE_CLUSTER: _ClassVar[StoreMode]
STORE_EVENT_TYPE_UNSPECIFIED: StoreEventType
STORE_EVENT_TYPE_ANNOUNCED: StoreEventType
STORE_EVENT_TYPE_RETIRED: StoreEventType
STORE_MODE_UNSPECIFIED: StoreMode
STORE_MODE_SINGLE: StoreMode
STORE_MODE_CLUSTER: StoreMode

class ListStoresRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListStoresResponse(_message.Message):
    __slots__ = ("instances",)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[StoreInstance]
    def __init__(self, instances: _Optional[_Iterable[_Union[StoreInstance, _Mapping]]] = ...) -> None: ...

class GetStoreRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class GetStoreResponse(_message.Message):
    __slots__ = ("instances",)
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[StoreInstance]
    def __init__(self, instances: _Optional[_Iterable[_Union[StoreInstance, _Mapping]]] = ...) -> None: ...

class WatchStoresRequest(_message.Message):
    __slots__ = ("include_snapshot",)
    INCLUDE_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    include_snapshot: bool
    def __init__(self, include_snapshot: _Optional[bool] = ...) -> None: ...

class StoreEvent(_message.Message):
    __slots__ = ("type", "instance", "event_at_us")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_AT_US_FIELD_NUMBER: _ClassVar[int]
    type: StoreEventType
    instance: StoreInstance
    event_at_us: int
    def __init__(self, type: _Optional[_Union[StoreEventType, str]] = ..., instance: _Optional[_Union[StoreInstance, _Mapping]] = ..., event_at_us: _Optional[int] = ...) -> None: ...

class StoreInstance(_message.Message):
    __slots__ = ("store_id", "node", "mode", "data_dir", "timeout_ms", "registered_at_us")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    DATA_DIR_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    REGISTERED_AT_US_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    node: str
    mode: StoreMode
    data_dir: str
    timeout_ms: int
    registered_at_us: int
    def __init__(self, store_id: _Optional[str] = ..., node: _Optional[str] = ..., mode: _Optional[_Union[StoreMode, str]] = ..., data_dir: _Optional[str] = ..., timeout_ms: _Optional[int] = ..., registered_at_us: _Optional[int] = ...) -> None: ...
