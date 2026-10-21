# Changelog

## Unreleased

- The quick start (README and the package docstring) built its events with
  `reckon_streams_pb2.ProposedEvent`, which does not exist: the message is in
  `reckon_shared_pb2`. It imports that module now. CI type-checks every Python
  block in the README and guides against the package (macula-codebase-checks#8),
  and a tag waits on it before it publishes.

## v0.2.0 (2026-09-26)

The first release on PyPI. `pip install reckon-py` failed before: neither
0.1.0 nor 0.1.1 was ever uploaded.

### Changed (breaking) — the import package is `reckon_db`

`import reckon` becomes `import reckon_db`, and `reckon._proto` becomes
`reckon_db._proto`. PyPI already has an unrelated package called `reckon` (a
caching library) that installs a top-level `reckon`, so the two could not be
installed side by side. The distribution name stays `reckon-py`, and the
gRPC wire (protobuf package `reckon.gateway.v1`) is unchanged. Nothing
depended on the old name, since it was never published.

### Changed — dependency floors are the versions the stubs need

`grpcio>=1.81.1` and `protobuf>=6.33.5,<7` (they said `grpcio>=1.60`,
`protobuf>=4.0`). The generated stubs refuse an older runtime at import, and
protobuf gencode refuses the next major, so the old floors let pip resolve an
environment where `import reckon_db` then failed. A test keeps the floors
equal to or above what the stubs were generated with; `grpcio-tools` is
pinned in the dev extra so a regeneration cannot move them silently. The
`.pyi` stubs import each other relatively now, so type checkers resolve them
through `py.typed`.

### Added — CI and a publish workflow

Every push and pull request runs the tests on Python 3.10 to 3.13, and builds
and checks the sdist and wheel, installs the wheel into a clean environment
at the dependency floors and at the latest, imports every stub module from
it and runs the tests against it. A `v*` tag publishes to PyPI through Trusted
Publishing (no stored token), and refuses a tag that disagrees with the
version in `pyproject.toml`.

## v0.1.1 (2026-09-02)

Not published to PyPI.

### Changed

- Project URLs point at `github.com/reckon-db-org/reckon-py`.
- `proto/` re-synced with reckon-proto 0.8.1 (`go_package` on the GitHub
  path) and `src/reckon/_proto/` regenerated from it. No wire change.

## v0.1.0 (2026-06-22)

Initial release (tagged, not published to PyPI).

- Packaged gRPC stubs for all ReckonDB services (generated from reckon-proto)
- `reckon.connect()` channel factory with TLS, insecure, and CA-cert options
- Expected-version sentinels: `AnyVersion`, `NoStream`, `StreamExists`
- DCB sentinel: `SEQ_CUTOFF_SAW_NOTHING`
- TagFilter helpers: `match_any`, `match_all`, `event_type`, `and_`, `or_`
- PEP 561 typed package (`py.typed`)
