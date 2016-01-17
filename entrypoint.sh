#!/bin/bash

if [ -n "$CREATE_DATABASE" ]; then
  bundle exec rake db:create
fi

if [ -n "$MIGRATE_DATABASE" ]; then
  bundle exec rake db:migrate
fi

exec "$@"
