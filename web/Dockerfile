FROM foxio/rails:4.2

ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN bundle install

WORKDIR /app
ADD . /app
