#!/bin/bash
# Versioned Gems
gem install annotate --version "~> 2.7.1" --no-rdoc
gem install json --version "~> 1.8" --no-rdoc

gem install uglifier --version ">= 1.3.0" --no-rdoc
gem install coffee-rails --version "~> 4.2.1" --no-rdoc
gem install jbuilder --version "~> 2.5" --no-rdoc
gem install sdoc --version "~> 0.4.0" --no-rdoc
gem install high_voltage --version "~> 3.0" --no-rdoc
gem install web-console --version "~> 2.0" --no-rdoc

gem install sass-rails --version "~> 5.0" --no-rdoc
gem install factory_girl_rails --version "~> 4.5.0" --no-rdoc
gem install rspec-rails --version "~> 3.5.1" --no-rdoc

gem install nokogiri --version "1.6.6.2" --no-rdoc
gem install mysql2 --version "~> 0.3.20" --no-rdoc

gem install unicorn --version "~> 5.0.1" --no-rdoc
gem install haml-rails --version "~> 0.9.0" --no-rdoc

# Unversioned Gems
gem install --no-rdoc bundler spring kaminari bullet guard guard-rspec guard-teaspoon \
  database_cleaner shoulda-matchers json_spec simplecov pg sqlite3 rubocop meta-tags \
  pry pry-nav timecop
