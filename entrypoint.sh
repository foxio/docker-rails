#!/bin/bash

if [ -n "$CREATE_DATABASE" ]; then
  echo "Creating the database..."
  bundle exec rake db:create
fi

if [ -n "$MIGRATE_DATABASE" ]; then
  echo "Migrating the database..."
  bundle exec rake db:migrate
fi

exec "$@"
