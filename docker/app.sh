#!/bin/bash
wait-for-it db:5432 --timeout=30 --strict -- echo "PostgreSQL is up"

alembic upgrade head

cd app
CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000