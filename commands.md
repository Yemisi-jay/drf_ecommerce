#commands

#packages
django
djangorestframework==3.15.2
python-dotenv==1.0.1
pytest==8.3.3
pytest-django 4.9.0
django-mptt
drf-spectacular
coverage
pytest-cov

django-admin startproject eCormmerce_project

python manage.py runserver

from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

pip install --upgrade pip

python manage.py spectacular --file schema.yml

