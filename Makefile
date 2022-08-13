APP = restapi

test:
	@flake8 . --exclude .venv

compose: test # dependencia do test
	@docker-compose build
	@docker-compose up