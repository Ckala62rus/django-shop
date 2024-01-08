1) install virtual env
python -m venv project_name

2) install django
pip install django==4.2.7

3) in to container django
docker exec -ti django_shop /bin/bash

4) django admin
django-admin

5) create new project
django-admin startproject project_name

6) run web server
python manage.py runserver 0.0.0.0:8000

7) run docker compose developer version
docker-compose -f docker-compose-dev.yml up -d
in to container: docker exec -ti django_shop_dev /bin/bash

8) run migrations
python manage.py migrate

9) delete all migration in module
./manage.py migrate my_app zero

10) delete migration on number igration
./manage.py migrate my_app 0010

11) show all migrations
python manage.py showmigrations

12) create migration
python manage.py makemigrations


