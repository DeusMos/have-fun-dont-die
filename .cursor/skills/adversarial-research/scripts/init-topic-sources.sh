#!/usr/bin/env bash
# Create sources/<mark>/ dirs. Marks live in AGENTS.md — do not copy filing-guide READMEs.
# Usage: init-topic-sources.sh topics/<slug>
#        init-topic-sources.sh compounds/<slug>
#        init-topic-sources.sh hallmarks/NN-short-name
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
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

mkdir -p "${dest}/sources"
for mark in "${MARKS[@]}"; do
  mkdir -p "${dest}/sources/${mark}"
done

echo "initialized ${rel}/sources (file notes under sources/<mark>/; marks in AGENTS.md)"
