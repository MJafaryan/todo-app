# TODO App
In this project we try to deploy a simple todo app with **django** and **django restframework**.

## Table of Contents
- [Features](#features)
- [Quick Start](#quick-start)
- [Development](#development)
    - [Project Structure](#project-structure)
    - [Commit Convention](#commit-convention)
- [Contributing](#contributing)
- [Contact Me](#contact-me)

## Features
- Restful API
- User-based Permission system
- Dockerized (Docker + Docker Compose)

## Quick Start
This project is **dockerized** and use **docker-compose**,
then for running the project just run the `docker-compose.yml` file in base directory with your code editor or the command below:

```
docker compose up
```

## Development
### Project Structure:
```
    todo-app
    ├── core
    │   ├── accounts
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── __init__.py
    │   │   ├── migrations
    │   │   │   ├── 0001_initial.py
    │   │   │   ├── __init__.py
    │   │   │   └── __pycache__
    │   │   │       ├── 0001_initial.cpython-312.pyc
    │   │   │       └── __init__.cpython-312.pyc
    │   │   ├── models.py
    │   │   ├── __pycache__
    │   │   │   ├── admin.cpython-312.pyc
    │   │   │   ├── apps.cpython-312.pyc
    │   │   │   ├── __init__.cpython-312.pyc
    │   │   │   └── models.cpython-312.pyc
    │   │   ├── tests.py
    │   │   └── views.py
    │   ├── core
    │   │   ├── asgi.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-312.pyc
    │   │   │   ├── settings.cpython-312.pyc
    │   │   │   └── urls.cpython-312.pyc
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── db.sqlite3
    │   ├── manage.py
    │   ├── requirements.txt
    │   └── tasks
    │       ├── admin.py
    │       ├── api
    │       │   ├── __init__.py
    │       │   ├── __pycache__
    │       │   │   └── __init__.cpython-312.pyc
    │       │   └── v1
    │       │       ├── __init__.py
    │       │       ├── __pycache__
    │       │       │   ├── __init__.cpython-312.pyc
    │       │       │   ├── serializers.cpython-312.pyc
    │       │       │   ├── urls.cpython-312.pyc
    │       │       │   └── views.cpython-312.pyc
    │       │       ├── serializers.py
    │       │       ├── urls.py
    │       │       └── views.py
    │       ├── apps.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   ├── 0001_initial.py
    │       │   ├── __init__.py
    │       │   └── __pycache__
    │       │       ├── 0001_initial.cpython-312.pyc
    │       │       └── __init__.cpython-312.pyc
    │       ├── models.py
    │       ├── __pycache__
    │       │   ├── admin.cpython-312.pyc
    │       │   ├── apps.cpython-312.pyc
    │       │   ├── __init__.cpython-312.pyc
    │       │   ├── models.cpython-312.pyc
    │       │   └── urls.cpython-312.pyc
    │       ├── tests.py
    │       ├── urls.py
    │       └── views.py
    ├── docker-compose.yml
    ├── LICENSE
    └── README.md
```

### Commit Convention:
This project uses [**Conventional Commits**](https://www.conventionalcommits.org/en/v1.0.0/) to write commits.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what what you'd like to modify or prove.

### Looking for Frontend Developer!
The backend for this Todo App is (*almost*) complete.
We're actively seeking a frontend developer to build the user interface.

## Contact Me
**M.Jafaryan**: m.jafaryan2006@gmail.com
