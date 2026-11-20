#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
STAGE=""
ALL=0
LIST=0
DRY_RUN=0
FORCE=0
DOWNLOADED=0
SKIPPED=0
FAILED=0

usage() {
  cat <<'EOF'
Usage: bash scripts/download_papers.sh (--stage 01|08|NN-slug | --all) [--list|--dry-run] [--force]
 --stage STAGE    Stage number or full stage folder name
 --all            All eight stages
 --list           Show papers and canonical arXiv URLs (offline)
 --dry-run        Show target filenames without downloading (offline)
 --force          Overwrite cached valid PDFs
 --help           Show this help
EOF
}

if [ "$#" -eq 0 ]; then usage >&2; exit 2; fi
while [ "$#" -gt 0 ]; do
  case "$1" in
    --stage) [ "$#" -ge 2 ] || { echo "missing stage" >&2; exit 2; }; STAGE="$2"; shift 2 ;;
    --all) ALL=1; shift ;;
    --list) LIST=1; shift ;;
    --dry-run) DRY_RUN=1; shift ;;
    --force) FORCE=1; shift ;;
    --help|-h) usage; exit 0 ;;
    *) echo "unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done
if { [ "$ALL" -eq 1 ] && [ -n "$STAGE" ]; } || { [ "$ALL" -eq 0 ] && [ -z "$STAGE" ]; }; then
  echo "specify exactly one of --stage and --all" >&2
  exit 2
fi

shopt -s nullglob
dirs=()
if [ "$ALL" -eq 1 ]; then
  dirs=( "$ROOT"/stages/[0-9][0-9]-* )
elif [[ "$STAGE" =~ ^[0-9]{1,2}$ ]]; then
  printf -v num '%02d' "$((10#$STAGE))"
  dirs=( "$ROOT"/stages/"$num"-* )
elif [[ "$STAGE" =~ ^[0-9][0-9]-[a-z0-9-]+$ ]]; then
  dirs=( "$ROOT/stages/$STAGE" )
else
  echo "invalid stage: $STAGE" >&2
  exit 2
fi
[ "${#dirs[@]}" -gt 0 ] || { echo "stage not found" >&2; exit 2; }
[ "$ALL" -eq 1 ] || [ "${#dirs[@]}" -eq 1 ] || { echo "ambiguous stage" >&2; exit 2; }

pdf_ok() {
  [ -s "$1" ] && [ "$(head -c 5 "$1")" = '%PDF-' ]
}

fetch() {
  local url="$1" output="$2"
  if command -v curl >/dev/null 2>&1; then
    curl -fsSL --retry 4 --retry-delay 2 --connect-timeout 20 --max-time 240 -o "$output" "$url"
  elif command -v wget >/dev/null 2>&1; then
    wget -q --tries=5 --timeout=40 -O "$output" "$url"
  else
    echo "curl or wget is required" >&2
    return 127
  fi
}
TEMP=""
cleanup() { [ -z "$TEMP" ] || rm -f "$TEMP"; }
trap cleanup EXIT

for dir in "${dirs[@]}"; do
  manifest="$dir/papers/core/manifest.tsv"
  out="$dir/papers/core/pdfs"
  if [ ! -f "$manifest" ]; then echo "missing manifest: $manifest" >&2; FAILED=$((FAILED+1)); continue; fi
  echo "==> $(basename "$dir")"
  while IFS=$'\t' read -r slug arxiv title || [ -n "$slug" ]; do
    if [ -z "$slug" ] || [ "$slug" = slug ] || [[ "$slug" == \#* ]]; then continue; fi
    if [[ ! "$slug" =~ ^[a-z0-9][a-z0-9-]*$ ]] || [[ ! "$arxiv" =~ ^[0-9]{4}\.[0-9]{4,5}(v[0-9]+)?$ ]]; then
      echo "invalid manifest row: $slug / $arxiv" >&2; FAILED=$((FAILED+1)); continue
    fi
    url="https://arxiv.org/pdf/$arxiv"
    target="$out/$slug--$arxiv.pdf"
    if [ "$LIST" -eq 1 ]; then printf '  %-12s %-30s %s\n    %s\n' "$arxiv" "$slug" "$title" "$url"; continue; fi
    if [ "$DRY_RUN" -eq 1 ]; then echo "  [DRY RUN] $url -> $target"; continue; fi
    mkdir -p "$out"
    if [ "$FORCE" -eq 0 ] && pdf_ok "$target"; then echo "  [SKIP] $(basename "$target")"; SKIPPED=$((SKIPPED+1)); continue; fi
    TEMP="$(mktemp "$out/.part.XXXXXXXX")"
    echo "  [GET] $title"
    if fetch "$url" "$TEMP" && pdf_ok "$TEMP"; then
      mv -f "$TEMP" "$target"; TEMP=""
      echo "  [OK] $(basename "$target")"
      DOWNLOADED=$((DOWNLOADED+1))
    else
      echo "  [FAIL] $url (network failure or non-PDF response)" >&2
      cleanup; TEMP=""
      FAILED=$((FAILED+1))
    fi
  done < "$manifest"
done
if [ "$LIST" -eq 0 ] && [ "$DRY_RUN" -eq 0 ]; then
  printf 'Summary: downloaded=%d skipped=%d failed=%d\n' "$DOWNLOADED" "$SKIPPED" "$FAILED"
fi
[ "$FAILED" -eq 0 ]
