up:
	docker-compose up -d

migrate:
	docker-compose run --rm django sh -c "python3 project/manage.py makemigrations; python3 project/manage.py migrate;"

test:
	docker-compose up -d && ./run.sh