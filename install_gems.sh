#!/bin/bash
gem install rails --version "~> 4.2.0"

# Versioned Gems
gem install annotate --version "~> 2.6.5"
gem install json --version "~> 1.8"
gem install sass-rails --version "~> 5.0"
gem install uglifier --version ">= 1.3.0"
gem install coffee-rails --version "~> 4.1.0"
gem install jbuilder --version "~> 2.0"
gem install sdoc --version "~> 0.4.0"
gem install letter_opener_web --version "~> 1.2.0"
gem install high_voltage --version "~> 2.2.1"
gem install factory_girl_rails --version "~> 4.2"
gem install rspec-rails --version "~> 3.4"
gem install web-console --version "~> 2.0"
gem install mysql2 --version "~> 0.3.20"

# Unversioned Gems
gem install bundler haml-rails spring kaminari bullet guard guard-rspec guard-teaspoon \
  letter_opener database_cleaner shoulda-matchers json_spec simplecov pg \
  sqlite3 unicorn rubocop meta-tags pry pry-nav timecop
