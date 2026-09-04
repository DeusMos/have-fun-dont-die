#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
export HFDD_ROOT="$(cd "$DIR/../.." && pwd)"
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-4}"
export ORT_NUM_THREADS="${ORT_NUM_THREADS:-4}"
if command -v uv >/dev/null 2>&1; then
  UV=uv
elif [[ -x "${HOME}/.local/bin/uv" ]]; then
  UV="${HOME}/.local/bin/uv"
else
  echo "uv is required to run docs-rag" >&2
  exit 1
fi
exec "$UV" --directory "$DIR" run python -m hfdd_docs_rag "$@"
