#!/usr/bin/env bash
# Regenerate gRPC stubs from proto/ into src/reckon_db/_proto/.
# Run from the repo root: ./scripts/gen_proto.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$SCRIPT_DIR/.."
PROTO_DIR="$ROOT/proto"
OUT_DIR="$ROOT/src/reckon_db/_proto"

mkdir -p "$OUT_DIR"

python3 -m grpc_tools.protoc \
  --proto_path="$PROTO_DIR" \
  --python_out="$OUT_DIR" \
  --grpc_python_out="$OUT_DIR" \
  --pyi_out="$OUT_DIR" \
  "$PROTO_DIR"/*.proto

# Fix relative imports: grpcio-tools emits absolute `import reckon_*_pb2`
# which fails when stubs live inside a package. Rewrite to relative in both
# _pb2.py and _pb2_grpc.py files.
cd "$OUT_DIR"
for f in *_pb2.py *_pb2_grpc.py; do
  sed -i 's/^import \(reckon_[a-z_]*_pb2\)/from . import \1/' "$f"
done

# Ensure the directory is a package.
touch __init__.py

echo "Generated stubs in $OUT_DIR"
