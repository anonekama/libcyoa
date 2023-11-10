#! /usr/bin/env bash

# Let the DB start
python ./libcyoa/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python ./libcyoa/initial_data.py