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
    ├── accounts
    │   ├── admin.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── v1
    │   │       ├── __init__.py
    │   │       ├── serializers.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── core
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── tasks
    │   ├── admin.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── v1
    │   │       ├── __init__.py
    │   │       ├── serializers.py
    │   │       ├── urls.py
    │   │       └── views.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── requirements.txt
    └── manage.py
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
