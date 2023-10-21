setup:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests

lint:
	pylint db_interact.py

all: setup lint test