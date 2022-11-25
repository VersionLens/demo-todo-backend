# Django backend for todo demo app

This demo backend is a Django server with GraphQL.

## Where's the frontend?

Check out [demo-todo-frontend](https://github.com/VersionLens/demo-todo-frontend) to get the frontend for this project.

## Prerequisites

-   Python 3.10
-   Poetry [installation guide](https://python-poetry.org/docs/#installation)

## Installation

Install dependences

```
poetry install
```

Activate virtualenv

```
poetry shell
```

Migrate data

```
python django/manage.py migrate
```

## Run

Activate virtualenv

```
poetry shell
```

Run server

```
python django/manage.py runserver
```
