SHELL := /bin/bash
.PHONY: init data baseline train deploy prepare-deployment test-endpoint
DEPLOYMENT_DIR := deployment-dir
POETRY_BIN := $(HOME)/.local/bin/poetry
init:
	@if ! command -v poetry &> /dev/null; then \
		echo "Poetry is not installed. Installing..."; \
		curl -sSL https://install.python-poetry.org | python3 -; \
	    echo 'export PATH="$(HOME)/.local/bin:$$PATH"' >> ~/.bashrc; \
	    source ~/.bashrc; \
	else \
		 echo "Poetry is already installed."; \
    fi
	@if ! $(POETRY_BIN) --version &> /dev/null; then \
         echo "Poetry could not run correctly. Please ensure Poetry is in your PATH, then try again."; \
         exit 1; \
    fi;
	poetry install || (poetry lock --no-update && poetry install)	
	
data:
	poetry run python src/data.py

baseline:
	poetry run python src/baseline_model.py

train:
	poetry run python src/train.py

prepare-deployment:
	rm -rf $(DEPLOYMENT_DIR) &&  cerebrium init $(DEPLOYMENT_DIR)
	poetry export -f requirements.txt --output $(DEPLOYMENT_DIR)/requirements.txt --without-hashes
	cp -r src/predict.py $(DEPLOYMENT_DIR)/main.py
	cp -r src $(DEPLOYMENT_DIR)/src/
	pip install cerebrium --upgrade # otherwise cerebrium deploy might fail

deploy: prepare-deployment
	cd $(DEPLOYMENT_DIR) && poetry run cerebrium deploy 

test-endpoint:
	poetry run python src/test_endpoint.py