create-virtualenv:
	python3 -m venv venv && source venv/bin/activate

install-package: create-virtualenv
	pip install .

unit-tests: install-package
	pytest tests/unit -v

integration-tests: install-package
	pytest tests/integration -v

e2e-tests: install-package
	pytest tests/e2e -v

tests: unit-tests integration-tests e2e-tests

run: install-package
	wordcounter-cli data/words.json

run-example: install-package
	wordcounter-cli --input-list 'apple, orange, grapes, apple, orange' data/words.json
