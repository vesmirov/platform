runserver:
	poetry run python manage.py runserver

gunicorn:
	poetry run yatube.wsgi:application -b 0:8000

makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic

createsuperuser:
	poetry run python manage.py createsuperuser

lint:
	poetry run flake8
