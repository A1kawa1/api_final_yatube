# api_final

## Description

This is a test project in which api technologies are implemented using the django framework

## Installation

Clone the repository and go to it on the command line:

```
git clone https://github.com/yandex-praktikum/kittygram_backend.git
```

```
cd kittygram_backend
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Install dependencies from a file requirements.txt:

```
pip install -r requirements.txt
```

Perform migrations:


```
python3 manage.py migrate
```

Launch a project:

```
python3 manage.py runserver
```
## Request examples

```
/api/v1/posts/ [GET, POST]
```

```
/api/v1/posts/{post_id}/comments/ [GET, POST]
```

```
/api/v1/jwt/create/ [POST]
```