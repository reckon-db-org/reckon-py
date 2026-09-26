# Changelog

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

### Added — CI and a publish workflow

Every push and pull request runs the tests on Python 3.10 to 3.13 and builds
and checks the sdist and wheel. A `v*` tag publishes to PyPI through Trusted
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
