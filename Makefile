deps:
	pipenv install

mypy: deps
	pipenv run mypy .
