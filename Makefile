run:
	pipenv run python main.py --incidents 'https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-27_daily_incident_summary.pdf'

test:
	pipenv run python -m pytest -v

test-unit:
	pipenv run python -m pytest -v -m "not integtest"

test-integ:
	pipenv run python -m pytest -v -m "integtest"

cov:
	pipenv run python -m pytest -v --cov=project0

lint:
	pipenv run python -m autopep8 --in-place --aggressive --aggressive --recursive .
