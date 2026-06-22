"""Unit tests for TagFilter helpers — no network required."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import reckon
from reckon._proto import reckon_dcb_pb2 as _pb


def test_match_any_single_tag():
    f = reckon.match_any("email:alice@example.com")
    assert f.HasField("match_any")
    assert list(f.match_any.tags) == ["email:alice@example.com"]


def test_match_any_multiple_tags():
    f = reckon.match_any("a", "b", "c")
    assert list(f.match_any.tags) == ["a", "b", "c"]


def test_match_all():
    f = reckon.match_all("tenant:t1", "role:admin")
    assert f.HasField("match_all")
    assert set(f.match_all.tags) == {"tenant:t1", "role:admin"}


def test_event_type():
    f = reckon.event_type("user_registered_v1")
    assert f.event_type_match == "user_registered_v1"


def test_and_composition():
    f = reckon.and_(reckon.event_type("seat_reserved_v1"), reckon.match_any("seat:FL-42:A3"))
    assert f.HasField("conjunction")
    inner = f.conjunction.filters
    assert len(inner) == 2
    assert inner[0].event_type_match == "seat_reserved_v1"
    assert list(inner[1].match_any.tags) == ["seat:FL-42:A3"]


def test_or_composition():
    f = reckon.or_(reckon.match_any("tag:a"), reckon.match_any("tag:b"))
    assert f.HasField("disjunction")
    assert len(f.disjunction.filters) == 2


def test_nested_composition():
    f = reckon.and_(
        reckon.event_type("item_reserved_v1"),
        reckon.or_(reckon.match_any("resource:R1"), reckon.match_all("zone:eu", "type:gpu")),
    )
    inner = f.conjunction.filters[1]
    assert inner.HasField("disjunction")


def test_returns_proto_type():
    f = reckon.match_any("x")
    assert isinstance(f, _pb.TagFilter)


def test_seq_cutoff_saw_nothing():
    assert reckon.SEQ_CUTOFF_SAW_NOTHING == -1


def test_version_sentinels():
    assert reckon.AnyVersion == -2
    assert reckon.NoStream == -1
    assert reckon.StreamExists == -4
