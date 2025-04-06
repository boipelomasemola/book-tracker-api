# Book Tracker API

A Django REST API for tracking books you've read, are reading, or want to read.

## Features
- User authentication (JWT)
- CRUD operations on books
- Personalized book lists

## Setup Instructions
1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the server: `python manage.py runserver`

## Endpoints
- `POST /api/token/` – Login
- `GET /api/books/` – View books
- `POST /api/books/` – Add book
- `PUT /api/books/<id>/` – Update book
- `DELETE /api/books/<id>/` – Delete book
