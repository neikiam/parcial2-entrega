
Sistema de gestión de estudiantes con scraper de Google Scholar.

En CMD:

```bash
py -3.10 -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
python --version
```

```bash
python -m pip install --upgrade pip
```

```bash
python -m pip install -U pip setuptools wheel
```

```bash
python -m pip install -r requirements.txt
```

Crear un .env basado en .env.example y luego

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```