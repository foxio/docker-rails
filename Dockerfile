FROM ruby:2.2.3

RUN apt-get update -qq && apt-get install -y build-essential libpq-dev \
  nodejs-legacy libmysqlclient-dev npm
RUN rm -rf /var/lib/apt/lists/*

RUN npm install bower -g
RUN mv /usr/local/bin/bower /usr/local/bin/bower_cli
COPY bower.sh /usr/local/bin/bower
RUN chmod +x /usr/local/bin/bower
ENV CI=true

COPY ./install_gems.sh /install_gems.sh
RUN bash /install_gems.sh
RUN rm -f /install_gems.sh

WORKDIR /app
ADD ./web /app
RUN bundle install

COPY ./unicorn.rb /etc/unicorn/unicorn.rb
COPY ./start_rails_app.sh /usr/bin/start_rails_app
RUN chmod +x /usr/bin/start_rails_app

EXPOSE 5000
CMD ["start_rails_app"]
