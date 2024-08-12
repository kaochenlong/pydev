.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: migration
migration:
	poetry run python manage.py makemigrations

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: shell
shell:
	poetry run python manage.py shell_plus --print-sql
