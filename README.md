## \***\*A Todo Backend application\*\***

> This is the backend implementation of the to-do list application. The API is implemented using the latest standards of Django, Django RESTful and Python.

## Features

- Django 4.3, djangorestframework 3.13, drf-nested-routers,
  django-cors-headers,
  social-auth-app-django,
  django-oauth-toolkit,
  drf-social-oauth2 & Python 3.9
- Install via [Pipenv](https://pypi.org/project/pip/)
- User social auth with Facebook.
- Logged in users will be able to mark an uncomplete to-do item as complete, and vise-versa.
- When a user logs in, he/she see a list of all her uncompleted to-do items.
- The user can use a toggle feature to toggle between uncompleted and completed items.
- The user can delete items from the to-do list
- Each person can only see the to-do items she creates for herself.

The code style used for the project is PEP 8 -- Style Guide for Python Code and Flake8: For Style Guide
Enforcement.

---

## Table of Contents

- **[Installation](#installation)**
  - [Pipenv](#pip)
- [Setup](#setup)

---

## Installation

The application can be installed via Pipenv. To start,
clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/Fachiis/todo-backend.git
$ cd todo-backend
```

```
$ pipenv install
$ pipenv shell
(todo-backend) $ python manage.py makemigrations
(todo-backend) $ python manage.py migrate
(todo-backend) $ python manage.py createsuperuser
(todo-backend) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000/api/v1
```

## Setup

```
# Run Migrations
(todo-backend) $ python manage.py migrate

# Create a Superuser
(todo-backend) $ python manage.py createsuperuser

# Confirm everything is working:
(todo-backend) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000/api/v1
```
