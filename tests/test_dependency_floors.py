"""The declared dependency floors are ones the shipped stubs actually run on.

The generated stubs guard their runtime: each _pb2.py calls
ValidateProtobufRuntimeVersion with the protobuf version that generated it,
and each _pb2_grpc.py refuses a grpcio older than GRPC_GENERATED_VERSION.
pyproject.toml declared grpcio>=1.60 and protobuf>=4.0, so pip resolved an
environment in which `import reckon_db` then raised. The floors must be at
least the generated versions, and protobuf below the next major, which the
gencode rejects too.
"""

import pathlib
import re
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROTO = ROOT / "src" / "reckon_db" / "_proto"


def _version(text):
    return tuple(int(p) for p in text.split("."))


def _requirement(name):
    deps = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["dependencies"]
    (spec,) = [d for d in deps if re.match(rf"{name}\b", d)]
    floor = re.search(r">=\s*([0-9.]+)", spec)
    upper = re.search(r"<\s*([0-9.]+)", spec)
    return _version(floor.group(1)), (_version(upper.group(1)) if upper else None)


def _generated_grpc():
    found = {re.search(r"GRPC_GENERATED_VERSION = '([0-9.]+)'", p.read_text()).group(1)
             for p in PROTO.glob("*_pb2_grpc.py")}
    assert len(found) == 1, found
    return _version(found.pop())


def _generated_protobuf():
    pattern = re.compile(r"ValidateProtobufRuntimeVersion\(\s*_runtime_version\.Domain\.PUBLIC,"
                         r"\s*(\d+),\s*(\d+),\s*(\d+),", re.S)
    found = {tuple(int(x) for x in pattern.search(p.read_text()).groups())
             for p in PROTO.glob("*_pb2.py")}
    assert len(found) == 1, found
    return found.pop()


def test_the_grpcio_floor_is_at_least_the_generated_version():
    floor, _ = _requirement("grpcio")
    assert floor >= _generated_grpc()


def test_the_protobuf_floor_is_at_least_the_generated_version_and_below_its_next_major():
    floor, upper = _requirement("protobuf")
    generated = _generated_protobuf()
    assert floor >= generated
    assert upper == (generated[0] + 1,)
