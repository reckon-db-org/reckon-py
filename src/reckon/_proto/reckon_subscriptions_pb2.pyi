import reckon_shared_pb2 as _reckon_shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscribeRequest(_message.Message):
    __slots__ = ("store_id", "type", "selector", "subscription_name", "start_from", "pool_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FROM_FIELD_NUMBER: _ClassVar[int]
    POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    type: _reckon_shared_pb2.SubscriptionType
    selector: str
    subscription_name: str
    start_from: int
    pool_size: int
    def __init__(self, store_id: _Optional[str] = ..., type: _Optional[_Union[_reckon_shared_pb2.SubscriptionType, str]] = ..., selector: _Optional[str] = ..., subscription_name: _Optional[str] = ..., start_from: _Optional[int] = ..., pool_size: _Optional[int] = ...) -> None: ...

class AckEventRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "subscription_name", "event_number")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    subscription_name: str
    event_number: int
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., subscription_name: _Optional[str] = ..., event_number: _Optional[int] = ...) -> None: ...

class CreateSubscriptionRequest(_message.Message):
    __slots__ = ("store_id", "type", "selector", "subscription_name", "start_from", "pool_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    START_FROM_FIELD_NUMBER: _ClassVar[int]
    POOL_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    type: _reckon_shared_pb2.SubscriptionType
    selector: str
    subscription_name: str
    start_from: int
    pool_size: int
    def __init__(self, store_id: _Optional[str] = ..., type: _Optional[_Union[_reckon_shared_pb2.SubscriptionType, str]] = ..., selector: _Optional[str] = ..., subscription_name: _Optional[str] = ..., start_from: _Optional[int] = ..., pool_size: _Optional[int] = ...) -> None: ...

class RemoveSubscriptionRequest(_message.Message):
    __slots__ = ("store_id", "type", "selector", "subscription_name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    type: _reckon_shared_pb2.SubscriptionType
    selector: str
    subscription_name: str
    def __init__(self, store_id: _Optional[str] = ..., type: _Optional[_Union[_reckon_shared_pb2.SubscriptionType, str]] = ..., selector: _Optional[str] = ..., subscription_name: _Optional[str] = ...) -> None: ...

class ListSubscriptionsRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ("store_id", "subscription_name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    subscription_name: str
    def __init__(self, store_id: _Optional[str] = ..., subscription_name: _Optional[str] = ...) -> None: ...

class GetSubscriptionLagRequest(_message.Message):
    __slots__ = ("store_id", "subscription_name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    subscription_name: str
    def __init__(self, store_id: _Optional[str] = ..., subscription_name: _Optional[str] = ...) -> None: ...

class SubscriptionEvent(_message.Message):
    __slots__ = ("event", "checkpoint")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    event: _reckon_shared_pb2.RecordedEvent
    checkpoint: int
    def __init__(self, event: _Optional[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]] = ..., checkpoint: _Optional[int] = ...) -> None: ...

class AckEventResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateSubscriptionResponse(_message.Message):
    __slots__ = ("subscription_id",)
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class RemoveSubscriptionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.SubscriptionInfo]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[_reckon_shared_pb2.SubscriptionInfo, _Mapping]]] = ...) -> None: ...

class GetSubscriptionLagResponse(_message.Message):
    __slots__ = ("lag", "current_checkpoint", "latest_version")
    LAG_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CHECKPOINT_FIELD_NUMBER: _ClassVar[int]
    LATEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    lag: int
    current_checkpoint: int
    latest_version: int
    def __init__(self, lag: _Optional[int] = ..., current_checkpoint: _Optional[int] = ..., latest_version: _Optional[int] = ...) -> None: ...
