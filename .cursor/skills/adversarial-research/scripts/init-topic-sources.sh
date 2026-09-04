#!/usr/bin/env bash
# Copy canonical sources/ READMEs into a hallmark, topic, or compound directory.
# Usage: init-topic-sources.sh topics/<slug>
#        init-topic-sources.sh compounds/<slug>
#        init-topic-sources.sh hallmarks/NN-short-name
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
CANON="${ROOT}/tmp/2026-09-02_layout/canonical/sources"
MARKS=(💯 📚 📜 🥼 🤔 🤼 ⛔ 🐉 ☠︎︎)

if [[ $# -ne 1 ]]; then
  echo "usage: $0 topics/<slug>|compounds/<slug>|hallmarks/NN-short-name" >&2
  exit 1
fi

rel="${1%/}"
dest="${ROOT}/${rel}"
if [[ "${rel}" != topics/* && "${rel}" != compounds/* && "${rel}" != hallmarks/* ]]; then
  echo "destination must be topics/<slug>, compounds/<slug>, or hallmarks/NN-short-name" >&2
  exit 1
fi

if [[ ! -d "${CANON}" ]]; then
  fallback="$(find "${ROOT}/hallmarks" -mindepth 2 -maxdepth 2 -type d -name sources | head -n 1 || true)"
  if [[ -z "${fallback}" ]]; then
    echo "missing canonical sources and no hallmark sources fallback" >&2
    exit 1
  fi
  CANON="${fallback}"
fi

if [[ ! -f "${CANON}/README.md" ]]; then
  echo "missing ${CANON}/README.md" >&2
  exit 1
fi

for mark in "${MARKS[@]}"; do
  if [[ ! -f "${CANON}/${mark}/README.md" ]]; then
    echo "missing ${CANON}/${mark}/README.md" >&2
    exit 1
  fi
done

mkdir -p "${dest}/sources"
cp "${CANON}/README.md" "${dest}/sources/README.md"
copied=0
for mark in "${MARKS[@]}"; do
  mkdir -p "${dest}/sources/${mark}"
  cp "${CANON}/${mark}/README.md" "${dest}/sources/${mark}/README.md"
  copied=$((copied + 1))
done

echo "initialized ${rel}/sources (${copied} mark READMEs from ${CANON})"
