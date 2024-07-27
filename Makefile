.PHONY: init data baseline train deploy prepare-deployment test-endpoint

DEPLOYMENT_DIR = deployment_dir

init:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install
	
data:
	poetry run python src/data.py
