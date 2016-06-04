.PHONY: lint test install develop migrate docker-build

PROJECT?=potion-test
PIP?=pip3
FLAKE8?=flake8
PYTEST?=py.test
PYTHON?=python3
COVERAGE?=true

install:
	$(PIP) install -r requirements.txt

lint:
	$(FLAKE8) --config=.flake8rc gateway_api

test: lint
ifeq ($(COVERAGE), true)
	$(PYTEST) --cov potion-test --cov-config .coveragerc --cov-report xml --junit-xml=results.xml test/
else
	$(PYTEST)
endif

develop: migrate
	$(PYTHON) manage.py runserver --host 0.0.0.0 --port 8888 --debug --reload

migrate:
	$(PYTHON) manage.py db upgrade
