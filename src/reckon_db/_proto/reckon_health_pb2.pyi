from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HealthStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HEALTH_STATUS_HEALTHY: _ClassVar[HealthStatus]
    HEALTH_STATUS_DEGRADED: _ClassVar[HealthStatus]
    HEALTH_STATUS_UNHEALTHY: _ClassVar[HealthStatus]

class ClusterStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLUSTER_STATUS_HEALTHY: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_DEGRADED: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_SPLIT_BRAIN: _ClassVar[ClusterStatus]
    CLUSTER_STATUS_NO_QUORUM: _ClassVar[ClusterStatus]

class MemoryLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEMORY_LEVEL_LOW: _ClassVar[MemoryLevel]
    MEMORY_LEVEL_NORMAL: _ClassVar[MemoryLevel]
    MEMORY_LEVEL_HIGH: _ClassVar[MemoryLevel]
    MEMORY_LEVEL_CRITICAL: _ClassVar[MemoryLevel]
HEALTH_STATUS_HEALTHY: HealthStatus
HEALTH_STATUS_DEGRADED: HealthStatus
HEALTH_STATUS_UNHEALTHY: HealthStatus
CLUSTER_STATUS_HEALTHY: ClusterStatus
CLUSTER_STATUS_DEGRADED: ClusterStatus
CLUSTER_STATUS_SPLIT_BRAIN: ClusterStatus
CLUSTER_STATUS_NO_QUORUM: ClusterStatus
MEMORY_LEVEL_LOW: MemoryLevel
MEMORY_LEVEL_NORMAL: MemoryLevel
MEMORY_LEVEL_HIGH: MemoryLevel
MEMORY_LEVEL_CRITICAL: MemoryLevel

class HealthCheckRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClusterCheckRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class MemoryLevelRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class MemoryStatsRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class HealthCheckResponse(_message.Message):
    __slots__ = ("status", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: HealthStatus
    details: _containers.ScalarMap[str, str]
    def __init__(self, status: _Optional[_Union[HealthStatus, str]] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("status", "stores", "total_workers", "node", "timestamp")
    class StoresEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STORES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WORKERS_FIELD_NUMBER: _ClassVar[int]
    NODE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: HealthStatus
    stores: _containers.ScalarMap[str, int]
    total_workers: int
    node: str
    timestamp: int
    def __init__(self, status: _Optional[_Union[HealthStatus, str]] = ..., stores: _Optional[_Mapping[str, int]] = ..., total_workers: _Optional[int] = ..., node: _Optional[str] = ..., timestamp: _Optional[int] = ...) -> None: ...

class ClusterCheckResponse(_message.Message):
    __slots__ = ("status", "details")
    class DetailsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    status: ClusterStatus
    details: _containers.ScalarMap[str, str]
    def __init__(self, status: _Optional[_Union[ClusterStatus, str]] = ..., details: _Optional[_Mapping[str, str]] = ...) -> None: ...

class MemoryLevelResponse(_message.Message):
    __slots__ = ("level",)
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: MemoryLevel
    def __init__(self, level: _Optional[_Union[MemoryLevel, str]] = ...) -> None: ...

class MemoryStatsResponse(_message.Message):
    __slots__ = ("used_bytes", "total_bytes", "usage_percent", "breakdown")
    class BreakdownEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    USAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    BREAKDOWN_FIELD_NUMBER: _ClassVar[int]
    used_bytes: int
    total_bytes: int
    usage_percent: float
    breakdown: _containers.ScalarMap[str, int]
    def __init__(self, used_bytes: _Optional[int] = ..., total_bytes: _Optional[int] = ..., usage_percent: _Optional[float] = ..., breakdown: _Optional[_Mapping[str, int]] = ...) -> None: ...

class GetServerInfoRequest(_message.Message):
    __slots__ = ("store_id",)
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    def __init__(self, store_id: _Optional[str] = ...) -> None: ...

class ServerInfoResponse(_message.Message):
    __slots__ = ("reckon_db_version", "reckon_gateway_version", "integrity_algo", "integrity_enabled", "hmac_key_id", "api_compatibility_version")
    RECKON_DB_VERSION_FIELD_NUMBER: _ClassVar[int]
    RECKON_GATEWAY_VERSION_FIELD_NUMBER: _ClassVar[int]
    INTEGRITY_ALGO_FIELD_NUMBER: _ClassVar[int]
    INTEGRITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HMAC_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    API_COMPATIBILITY_VERSION_FIELD_NUMBER: _ClassVar[int]
    reckon_db_version: str
    reckon_gateway_version: str
    integrity_algo: str
    integrity_enabled: bool
    hmac_key_id: int
    api_compatibility_version: str
    def __init__(self, reckon_db_version: _Optional[str] = ..., reckon_gateway_version: _Optional[str] = ..., integrity_algo: _Optional[str] = ..., integrity_enabled: _Optional[bool] = ..., hmac_key_id: _Optional[int] = ..., api_compatibility_version: _Optional[str] = ...) -> None: ...
