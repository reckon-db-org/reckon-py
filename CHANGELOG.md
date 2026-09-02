# Changelog

## v0.1.1 (2026-09-02)

### Changed

- Project URLs point at `github.com/reckon-db-org/reckon-py`.
- `proto/` re-synced with reckon-proto 0.8.1 (`go_package` on the GitHub
  path) and `src/reckon/_proto/` regenerated from it. No wire change.

## v0.1.0 (2026-06-22)

Initial release.

- Packaged gRPC stubs for all ReckonDB services (generated from reckon-proto)
- `reckon.connect()` channel factory with TLS, insecure, and CA-cert options
- Expected-version sentinels: `AnyVersion`, `NoStream`, `StreamExists`
- DCB sentinel: `SEQ_CUTOFF_SAW_NOTHING`
- TagFilter helpers: `match_any`, `match_all`, `event_type`, `and_`, `or_`
- PEP 561 typed package (`py.typed`)
