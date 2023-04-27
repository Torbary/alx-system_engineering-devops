#!/usr/bin/env bash
# use puppet for 3-redirection operation

# Install Nginx and set it to listen on port 80
class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    content => "
server {
    listen 80;
    listen [::]:80 default_server;
    root   /var/www/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.google.com;
    }
}
",
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

include nginx
