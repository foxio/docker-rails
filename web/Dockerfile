FROM foxio/rails

COPY Gemfile /app/Gemfile
COPY Gemfile.lock /app/Gemfile.lock
RUN bundle install

WORKDIR /app
COPY . /app
