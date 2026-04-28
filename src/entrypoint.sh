#!/bin/sh
python -c "from database import engine; from models import Base; Base.metadata.create_all(bind=engine)"
python seed.py
uvicorn main:app --host 0.0.0.0 --port 8000