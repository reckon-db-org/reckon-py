from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBSCRIPTION_TYPE_UNSPECIFIED: _ClassVar[SubscriptionType]
    SUBSCRIPTION_TYPE_STREAM: _ClassVar[SubscriptionType]
    SUBSCRIPTION_TYPE_EVENT_TYPE: _ClassVar[SubscriptionType]
    SUBSCRIPTION_TYPE_EVENT_PATTERN: _ClassVar[SubscriptionType]
    SUBSCRIPTION_TYPE_EVENT_PAYLOAD: _ClassVar[SubscriptionType]
    SUBSCRIPTION_TYPE_TAGS: _ClassVar[SubscriptionType]

class TagMatch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TAG_MATCH_ANY: _ClassVar[TagMatch]
    TAG_MATCH_ALL: _ClassVar[TagMatch]
SUBSCRIPTION_TYPE_UNSPECIFIED: SubscriptionType
SUBSCRIPTION_TYPE_STREAM: SubscriptionType
SUBSCRIPTION_TYPE_EVENT_TYPE: SubscriptionType
SUBSCRIPTION_TYPE_EVENT_PATTERN: SubscriptionType
SUBSCRIPTION_TYPE_EVENT_PAYLOAD: SubscriptionType
SUBSCRIPTION_TYPE_TAGS: SubscriptionType
TAG_MATCH_ANY: TagMatch
TAG_MATCH_ALL: TagMatch

class ProposedEvent(_message.Message):
    __slots__ = ("event_id", "event_type", "data", "metadata", "tags", "data_content_type", "metadata_content_type")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DATA_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    event_type: str
    data: bytes
    metadata: bytes
    tags: _containers.RepeatedScalarFieldContainer[str]
    data_content_type: str
    metadata_content_type: str
    def __init__(self, event_id: _Optional[str] = ..., event_type: _Optional[str] = ..., data: _Optional[bytes] = ..., metadata: _Optional[bytes] = ..., tags: _Optional[_Iterable[str]] = ..., data_content_type: _Optional[str] = ..., metadata_content_type: _Optional[str] = ...) -> None: ...

class RecordedEvent(_message.Message):
    __slots__ = ("event_id", "event_type", "stream_id", "version", "data", "metadata", "tags", "timestamp", "epoch_us", "data_content_type", "metadata_content_type", "prev_event_hash")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EPOCH_US_FIELD_NUMBER: _ClassVar[int]
    DATA_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    METADATA_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREV_EVENT_HASH_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    event_type: str
    stream_id: str
    version: int
    data: bytes
    metadata: bytes
    tags: _containers.RepeatedScalarFieldContainer[str]
    timestamp: int
    epoch_us: int
    data_content_type: str
    metadata_content_type: str
    prev_event_hash: bytes
    def __init__(self, event_id: _Optional[str] = ..., event_type: _Optional[str] = ..., stream_id: _Optional[str] = ..., version: _Optional[int] = ..., data: _Optional[bytes] = ..., metadata: _Optional[bytes] = ..., tags: _Optional[_Iterable[str]] = ..., timestamp: _Optional[int] = ..., epoch_us: _Optional[int] = ..., data_content_type: _Optional[str] = ..., metadata_content_type: _Optional[str] = ..., prev_event_hash: _Optional[bytes] = ...) -> None: ...

class SnapshotRecord(_message.Message):
    __slots__ = ("stream_id", "version", "data", "metadata", "timestamp", "anchor_hash")
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_HASH_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    version: int
    data: bytes
    metadata: bytes
    timestamp: int
    anchor_hash: bytes
    def __init__(self, stream_id: _Optional[str] = ..., version: _Optional[int] = ..., data: _Optional[bytes] = ..., metadata: _Optional[bytes] = ..., timestamp: _Optional[int] = ..., anchor_hash: _Optional[bytes] = ...) -> None: ...

class SubscriptionInfo(_message.Message):
    __slots__ = ("id", "type", "selector", "subscription_name", "created_at", "pool_size", "checkpoint")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: SubscriptionType
    selector: str
    subscription_name: str
    created_at: int
    pool_size: int
    checkpoint: int
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[SubscriptionType, str]] = ..., selector: _Optional[str] = ..., subscription_name: _Optional[str] = ..., created_at: _Optional[int] = ..., pool_size: _Optional[int] = ..., checkpoint: _Optional[int] = ...) -> None: ...
