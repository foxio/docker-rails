#!/bin/bash

if [ -z "$RAILS_ENV" ]; then
  export RAILS_ENV="development"
fi

if [ "$DEBUG" = "true" ]; then
  echo -n "" > /app/log/unicorn.stderr.log
  echo -n "" > /app/log/$RAILS_ENV.log
  tail -n1 -f "log/$RAILS_ENV.log" &
  tail -n1 -f log/unicorn.stderr.log &
fi

echo "`rails --version`: `ruby --version`"
echo "Unicorn starting for ${RAILS_ENV}... "
bundle exec unicorn -E $RAILS_ENV -p 5000 -o 0.0.0.0 \
  -c /etc/unicorn/unicorn.rb
exit $?
