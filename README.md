
Sistema de gestión de estudiantes con scraper de Google Scholar.

En CMD:

py -3.10 -m venv .venv
.venv\Scripts\activate
python --version
python -m pip install --upgrade pip
python -m pip install -U pip setuptools wheel
python -m pip install -r requirements.txt

Crear un .env basado en .env.example y luego

python manage.py makemigrations
python manage.py migrate
python manage.py runserver