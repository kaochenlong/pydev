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

.PHONY: routes
routes:
	poetry run python manage.py show_urls

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: commit
commit:
	poetry run cz commit

.PHONY: init_db
init_db:
	poetry run python manage.py init_db
