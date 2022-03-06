run:
	pipenv run python main.py --incidents 'https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-27_daily_incident_summary.pdf'

test:
	pipenv run python -m pytest -v

cov:
	pipenv run python -m pytest -v --cov=project0

lint:
	pipenv run python -m autopep8 --in-place --aggressive --aggressive --recursive .
