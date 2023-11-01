startvenv:
	.\venv\Scripts\activate

run:
	.\venv\Scripts\python.exe .\manage.py runserver  

test:
	coverage run .\manage.py test

coverage:
	coverage html	

makemigrations:
	.\venv\Scripts\python.exe .\manage.py makemigrations

migrate:
	.\venv\Scripts\python.exe .\manage.py migrate

.PHONY: startvenv run test coverage makemigrations migrate