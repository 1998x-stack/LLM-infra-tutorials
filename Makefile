.PHONY: validate test papers papers-list papers-dryrun index help
STAGE ?= 07
help:
	@echo 'make validate                   Run offline integrity checks'
	@echo 'make papers STAGE=07            Download stage core PDFs'
	@echo 'make papers-list STAGE=05       List stage papers'
	@echo 'make papers-dryrun              Preview PDF downloads'
validate:
	python3 scripts/validate_repo.py
	python3 -m unittest discover -s tests -v
test:
	python3 -m unittest discover -s tests -v
papers:
	bash scripts/download_papers.sh --stage $(STAGE)
papers-list:
	bash scripts/download_papers.sh --stage $(STAGE) --list
papers-dryrun:
	bash scripts/download_papers.sh --all --dry-run
index:
	python3 scripts/list_papers.py
