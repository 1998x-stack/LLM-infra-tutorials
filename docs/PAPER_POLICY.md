# Paper download and provenance

Stage-specific `papers/core/manifest.tsv` has tab-separated fields:

```text
slug<TAB>arxiv_id<TAB>title
```

Run one stage's downloader from anywhere:

```bash
bash stages/07-inference-optimization/papers/core/download.sh --list
bash stages/07-inference-optimization/papers/core/download.sh --dry-run
bash stages/07-inference-optimization/papers/core/download.sh
```

Or use the root script:

```bash
bash scripts/download_papers.sh --stage 07
bash scripts/download_papers.sh --all --dry-run
bash scripts/download_papers.sh --all --force
```

The downloader builds `https://arxiv.org/pdf/<id>`, retries transient errors, checks the PDF signature, atomically moves completed downloads and skips valid existing files. It needs Bash 4+ and either curl or wget. CI does not download PDFs.

Downloaded PDFs are git-ignored. Preserve author copyright and check the original paper/version when reproducing. The TSV manifest is the source of truth; wiki entries mirror these identifiers.

**No network is needed for `make validate`.**
