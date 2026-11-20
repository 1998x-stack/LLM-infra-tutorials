.PHONY: validate test papers papers-list papers-dryrun index skills-sync skills-check help
STAGE ?= 07
help:
	@echo 'make validate                   Run offline structural and unit checks'
	@echo 'make skills-sync                Copy canonical skills to five client layouts'
	@echo 'make skills-check               Verify mirrors + routing test fixtures'
	@echo 'make papers STAGE=07            Download stage core PDFs'
	@echo 'make papers-list STAGE=05       List stage papers'
	@echo 'make papers-dryrun              Preview PDF downloads'
validate:
	python3 scripts/validate_repo.py
	python3 scripts/sync_agent_skills.py --check
	python3 scripts/validate_skill_cases.py
	python3 scripts/build_knowledge_index.py --check
	python3 -m unittest discover -s tests -v
skills-sync:
	python3 scripts/sync_agent_skills.py
skills-check:
	python3 scripts/sync_agent_skills.py --check
	python3 scripts/validate_skill_cases.py
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

