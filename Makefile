install:
	pip install --upgrade pip --quiet && pip install -r requirements.txt --quiet

format:
	black .

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py . 

test:
	python -m pytest --cov=main test_main.py

all: install format lint test

