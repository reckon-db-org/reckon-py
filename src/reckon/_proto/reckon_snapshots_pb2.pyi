import reckon_shared_pb2 as _reckon_shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecordSnapshotRequest(_message.Message):
    __slots__ = ("store_id", "source_uuid", "stream_uuid", "version", "data", "metadata")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    STREAM_UUID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    source_uuid: str
    stream_uuid: str
    version: int
    data: bytes
    metadata: bytes
    def __init__(self, store_id: _Optional[str] = ..., source_uuid: _Optional[str] = ..., stream_uuid: _Optional[str] = ..., version: _Optional[int] = ..., data: _Optional[bytes] = ..., metadata: _Optional[bytes] = ...) -> None: ...

class ReadSnapshotRequest(_message.Message):
    __slots__ = ("store_id", "source_uuid", "stream_uuid", "version")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    STREAM_UUID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    source_uuid: str
    stream_uuid: str
    version: int
    def __init__(self, store_id: _Optional[str] = ..., source_uuid: _Optional[str] = ..., stream_uuid: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ("store_id", "source_uuid", "stream_uuid", "version")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    STREAM_UUID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    source_uuid: str
    stream_uuid: str
    version: int
    def __init__(self, store_id: _Optional[str] = ..., source_uuid: _Optional[str] = ..., stream_uuid: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class ListSnapshotsRequest(_message.Message):
    __slots__ = ("store_id", "source_uuid", "stream_uuid")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_UUID_FIELD_NUMBER: _ClassVar[int]
    STREAM_UUID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    source_uuid: str
    stream_uuid: str
    def __init__(self, store_id: _Optional[str] = ..., source_uuid: _Optional[str] = ..., stream_uuid: _Optional[str] = ...) -> None: ...

class ListAllSnapshotsRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class RecordSnapshotResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSnapshotsResponse(_message.Message):
    __slots__ = ("snapshots",)
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.SnapshotRecord]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[_reckon_shared_pb2.SnapshotRecord, _Mapping]]] = ...) -> None: ...
