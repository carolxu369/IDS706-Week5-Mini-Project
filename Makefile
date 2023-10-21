setup:
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests

run:
    python3 your_script_name.py