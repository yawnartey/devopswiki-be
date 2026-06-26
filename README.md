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

![Backend Architecture](diagrams/architecture.svg)
