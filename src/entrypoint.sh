#!/bin/sh
python seed.py
python crawler.py
uvicorn main:app --host 0.0.0.0 --port 8000