rails_env = ENV['RAILS_ENV']
app_dir = '/app'

working_directory app_dir
worker_processes rails_env == 'production' ? 4 : 1
timeout 15
preload_app true

# pid "#{app_dir}/tmp/unicorn.pid"
listen '/tmp/unicorn.sock', backlog: 64
stderr_path "#{app_dir}/log/unicorn.stderr.log"
stdout_path "#{app_dir}/log/unicorn.stdout.log"

before_fork do |_server, _worker|
  Signal.trap 'TERM' do
    puts 'Unicorn master intercepting TERM and sending myself QUIT instead'
    Process.kill 'QUIT', Process.pid
  end

  defined?(ActiveRecord::Base) && ActiveRecord::Base.connection.disconnect!
end

after_fork do |_server, _worker|
  Signal.trap 'TERM' do
    puts 'Unicorn worker intercepting TERM and doing nothing. Wait for master
          to send QUIT'
  end

  defined?(ActiveRecord::Base) && ActiveRecord::Base.establish_connection
end
