test:
	pipenv run python -m pytest -v

test-unit:
	pipenv run python -m pytest -v -m "not integtest"

test-integ:
	pipenv run python -m pytest -v -m "integtest"

cov:
	pipenv run python -m pytest -v --cov=project0
