.PHONY: server
server:
	poetry run python manage.py runserver

.PHONY: migration
migration:
	poetry run python manage.py makemigrations

.PHONY: shell
shell:
	poetry run python manage.py shell
