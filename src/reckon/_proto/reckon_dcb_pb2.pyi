import reckon_shared_pb2 as _reckon_shared_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TagFilter(_message.Message):
    __slots__ = ("match_any", "match_all", "conjunction", "disjunction", "event_type_match")
    MATCH_ANY_FIELD_NUMBER: _ClassVar[int]
    MATCH_ALL_FIELD_NUMBER: _ClassVar[int]
    CONJUNCTION_FIELD_NUMBER: _ClassVar[int]
    DISJUNCTION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_MATCH_FIELD_NUMBER: _ClassVar[int]
    match_any: TagList
    match_all: TagList
    conjunction: FilterList
    disjunction: FilterList
    event_type_match: str
    def __init__(self, match_any: _Optional[_Union[TagList, _Mapping]] = ..., match_all: _Optional[_Union[TagList, _Mapping]] = ..., conjunction: _Optional[_Union[FilterList, _Mapping]] = ..., disjunction: _Optional[_Union[FilterList, _Mapping]] = ..., event_type_match: _Optional[str] = ...) -> None: ...

class TagList(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags: _Optional[_Iterable[str]] = ...) -> None: ...

class FilterList(_message.Message):
    __slots__ = ("filters",)
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    filters: _containers.RepeatedCompositeFieldContainer[TagFilter]
    def __init__(self, filters: _Optional[_Iterable[_Union[TagFilter, _Mapping]]] = ...) -> None: ...

class AppendIfNoTagMatchesRequest(_message.Message):
    __slots__ = ("store_id", "tag_filter", "seq_cutoff", "events")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FILTER_FIELD_NUMBER: _ClassVar[int]
    SEQ_CUTOFF_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    tag_filter: TagFilter
    seq_cutoff: int
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.ProposedEvent]
    def __init__(self, store_id: _Optional[str] = ..., tag_filter: _Optional[_Union[TagFilter, _Mapping]] = ..., seq_cutoff: _Optional[int] = ..., events: _Optional[_Iterable[_Union[_reckon_shared_pb2.ProposedEvent, _Mapping]]] = ...) -> None: ...

class AppendIfNoTagMatchesResponse(_message.Message):
    __slots__ = ("committed", "conflict")
    COMMITTED_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_FIELD_NUMBER: _ClassVar[int]
    committed: Committed
    conflict: Conflict
    def __init__(self, committed: _Optional[_Union[Committed, _Mapping]] = ..., conflict: _Optional[_Union[Conflict, _Mapping]] = ...) -> None: ...

class Committed(_message.Message):
    __slots__ = ("last_seq",)
    LAST_SEQ_FIELD_NUMBER: _ClassVar[int]
    last_seq: int
    def __init__(self, last_seq: _Optional[int] = ...) -> None: ...

class Conflict(_message.Message):
    __slots__ = ("max_seq",)
    MAX_SEQ_FIELD_NUMBER: _ClassVar[int]
    max_seq: int
    def __init__(self, max_seq: _Optional[int] = ...) -> None: ...

class ReadDcbContextRequest(_message.Message):
    __slots__ = ("store_id", "tag_filter", "batch_size")
    STORE_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FILTER_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    store_id: str
    tag_filter: TagFilter
    batch_size: int
    def __init__(self, store_id: _Optional[str] = ..., tag_filter: _Optional[_Union[TagFilter, _Mapping]] = ..., batch_size: _Optional[int] = ...) -> None: ...

class ReadDcbContextResponse(_message.Message):
    __slots__ = ("events", "max_seq")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_SEQ_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_reckon_shared_pb2.RecordedEvent]
    max_seq: int
    def __init__(self, events: _Optional[_Iterable[_Union[_reckon_shared_pb2.RecordedEvent, _Mapping]]] = ..., max_seq: _Optional[int] = ...) -> None: ...
