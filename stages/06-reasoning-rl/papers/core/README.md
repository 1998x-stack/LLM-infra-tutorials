# Stage 06 — Core papers

`manifest.tsv` contains the core source of truth. PDF downloads are stored under `pdfs/` and intentionally git-ignored.

```bash
bash stages/06-reasoning-rl/papers/core/download.sh --list
bash stages/06-reasoning-rl/papers/core/download.sh --dry-run
bash stages/06-reasoning-rl/papers/core/download.sh
```

Do not commit downloaded PDFs. Pin arXiv versions when an experiment depends on a specific revision.

Paper notes belong in `wiki/papers/`, linked using the same stable paper slug.
