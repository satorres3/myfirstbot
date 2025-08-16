.PHONY: run migrate docs

run:
	python manage.py runserver

migrate:
	python manage.py migrate

docs:
	$(MAKE) -C docs html
