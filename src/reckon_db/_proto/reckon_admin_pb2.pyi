from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoreStatsRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class StoreStatsResponse(_message.Message):
    __slots__ = ("total_streams", "total_events", "total_subscriptions", "total_snapshots", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TOTAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_EVENTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    total_streams: int
    total_events: int
    total_subscriptions: int
    total_snapshots: int
    details: _containers.ScalarMap[str, str]
    def __init__(self, total_streams: _Optional[int] = ..., total_events: _Optional[int] = ..., total_subscriptions: _Optional[int] = ..., total_snapshots: _Optional[int] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...

class StreamInfoRequest(_message.Message):
    __slots__ = ("store_id", "stream_id")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ...) -> None: ...

class StreamInfoResponse(_message.Message):
    __slots__ = ("stream_id", "version", "event_count", "created_at", "last_event_at", "event_types")
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_EVENT_AT_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    stream_id: str
    version: int
    event_count: int
    created_at: int
    last_event_at: int
    event_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, stream_id: _Optional[str] = ..., version: _Optional[int] = ..., event_count: _Optional[int] = ..., created_at: _Optional[int] = ..., last_event_at: _Optional[int] = ..., event_types: _Optional[_Iterable[str]] = ...) -> None: ...

class EventTypeSummaryRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class EventTypeSummaryEntry(_message.Message):
    __slots__ = ("event_type", "count")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    event_type: str
    count: int
    def __init__(self, event_type: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class EventTypeSummaryResponse(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[EventTypeSummaryEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[EventTypeSummaryEntry, _Mapping]]] = ...) -> None: ...

class ScavengeRequest(_message.Message):
    __slots__ = ("store_id", "stream_id", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    stream_id: str
    options: _containers.ScalarMap[str, str]
    def __init__(self, store_id: _Optional[str] = ..., stream_id: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ScavengeResponse(_message.Message):
    __slots__ = ("events_removed", "events_remaining", "space_reclaimed_bytes", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    EVENTS_REMOVED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    SPACE_RECLAIMED_BYTES_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    events_removed: int
    events_remaining: int
    space_reclaimed_bytes: int
    details: _containers.ScalarMap[str, str]
    def __init__(self, events_removed: _Optional[int] = ..., events_remaining: _Optional[int] = ..., space_reclaimed_bytes: _Optional[int] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ScavengeMatchingRequest(_message.Message):
    __slots__ = ("store_id", "pattern", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    pattern: str
    options: _containers.ScalarMap[str, str]
    def __init__(self, store_id: _Optional[str] = ..., pattern: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ScavengeMatchingResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[ScavengeResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[ScavengeResponse, _Mapping]]] = ...) -> None: ...

class CreateLinkRequest(_message.Message):
    __slots__ = ("store_id", "name", "source", "target", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    source: str
    target: str
    options: _containers.ScalarMap[str, str]
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteLinkRequest(_message.Message):
    __slots__ = ("store_id", "name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLinkRequest(_message.Message):
    __slots__ = ("store_id", "name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class LinkInfo(_message.Message):
    __slots__ = ("name", "source", "target", "options")
    class OptionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    source: str
    target: str
    options: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., source: _Optional[str] = ..., target: _Optional[str] = ..., options: _Optional[_Mapping[str, str]] = ...) -> None: ...

class StartLinkRequest(_message.Message):
    __slots__ = ("store_id", "name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class StartLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StopLinkRequest(_message.Message):
    __slots__ = ("store_id", "name")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    name: str
    def __init__(self, store_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class StopLinkResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLinksRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class ListLinksResponse(_message.Message):
    __slots__ = ("links",)
    LINKS_FIELD_NUMBER: _ClassVar[int]
    links: _containers.RepeatedCompositeFieldContainer[LinkInfo]
    def __init__(self, links: _Optional[_Iterable[_Union[LinkInfo, _Mapping]]] = ...) -> None: ...

class LinkRuntimeInfo(_message.Message):
    __slots__ = ("name", "status", "events_processed", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    status: str
    events_processed: int
    details: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., status: _Optional[str] = ..., events_processed: _Optional[int] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ReloadCatalogueRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReloadCatalogueResponse(_message.Message):
    __slots__ = ("added", "removed", "restarted", "error")
    ADDED_FIELD_NUMBER: _ClassVar[int]
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    RESTARTED_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    added: _containers.RepeatedScalarFieldContainer[str]
    removed: _containers.RepeatedScalarFieldContainer[str]
    restarted: _containers.RepeatedScalarFieldContainer[str]
    error: str
    def __init__(self, added: _Optional[_Iterable[str]] = ..., removed: _Optional[_Iterable[str]] = ..., restarted: _Optional[_Iterable[str]] = ..., error: _Optional[str] = ...) -> None: ...

class GetCatalogueStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCatalogueStatusResponse(_message.Message):
    __slots__ = ("catalogue_size", "gateway_uptime_ms", "clusters")
    CATALOGUE_SIZE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_UPTIME_MS_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    catalogue_size: int
    gateway_uptime_ms: int
    clusters: _containers.RepeatedCompositeFieldContainer[CatalogueClusterStatus]
    def __init__(self, catalogue_size: _Optional[int] = ..., gateway_uptime_ms: _Optional[int] = ..., clusters: _Optional[_Iterable[_Union[CatalogueClusterStatus, _Mapping]]] = ...) -> None: ...

class CatalogueClusterStatus(_message.Message):
    __slots__ = ("cluster_id", "members", "store_count", "status", "last_refresh", "last_error")
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    STORE_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    cluster_id: str
    members: _containers.RepeatedScalarFieldContainer[str]
    store_count: int
    status: str
    last_refresh: str
    last_error: str
    def __init__(self, cluster_id: _Optional[str] = ..., members: _Optional[_Iterable[str]] = ..., store_count: _Optional[int] = ..., status: _Optional[str] = ..., last_refresh: _Optional[str] = ..., last_error: _Optional[str] = ...) -> None: ...
