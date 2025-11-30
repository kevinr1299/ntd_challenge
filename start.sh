#!/bin/sh
set -e

echo "> Applying migrations"
python manage.py migrate
echo

# Run (keep alive process)
gunicorn ntd_challenge.wsgi:application -w 4 -b 0.0.0.0:8000 --timeout 300 --reload --log-level debug
