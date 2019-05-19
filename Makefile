build:
	docker-compose build
run:
	docker-compose up
fmt:
	isort -rc . && black .
