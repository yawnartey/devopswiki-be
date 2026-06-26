# DevOpsWiki Backend

REST API for the DevOpsWiki application, built with FastAPI and PostgreSQL.

## Stack

- **FastAPI** - API framework
- **SQLAlchemy** - ORM
- **PostgreSQL** - Database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

## Prerequisites

- Python 3.10+
- PostgreSQL database

## Structure

```
src/
├── main.py              # App entry point — registers router, creates tables
├── database.py          # SQLAlchemy engine, session factory, Base
├── models.py            # Resource ORM model
├── schema.py            # Pydantic schemas for request/response validation
├── seed.py              # Initial resource data loader
├── entrypoint.sh        # Container startup script
├── Dockerfile           # Container image definition
└── routes/
    └── resources.py     # API route handlers
```

## Architecture

<br>

![Backend Architecture](diagrams/devopswiki-be-5.png)

<br>

## Environment Variables

Create a .env file in src/ with the following:
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>

## Running Locally

cd src

### Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate

### Install dependencies

pip install -r requirement.txt

### Set up environment

cp .env.example .env # then fill in DATABASE_URL

### Create tables and seed data

python seed.py

### Start the server

uvicorn main:app --reload --port 8000
API will be available at http://localhost:8000.

Interactive docs at http://localhost:8000/docs.

## Running with Docker

cd src

### Build the image

docker build -t devopswiki-be .

### Run the container

docker run -d \
 -p 8000:8000 \
 -e DATABASE_URL=postgresql://user:pass@host:5432/dbname \
 devopswiki-be
