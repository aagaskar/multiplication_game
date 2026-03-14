#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"
uv run gunicorn --bind 0.0.0.0:8000 --workers 2 app:app
