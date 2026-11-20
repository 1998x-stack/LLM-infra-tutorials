#!/usr/bin/env bash
set -Eeuo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
root="$(cd "$here/../../../.." && pwd)"
exec bash "$root/scripts/download_papers.sh" --stage "03-pretraining-scaling" "$@"
