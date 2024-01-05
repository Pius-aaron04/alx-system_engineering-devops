# Manifest Installs and configures Nginx Web server

$nginx_config=@(EOF)
server{
    listen 80 default_server;
    root /var/www//html;
    index index.html;
    rewrite ^/redirect_me https://github.com/pius-aaron04 permanent;
}
EOF
class webserver::nginx{

  package{'nginx':
    ensure   => installed,
    provider => "apt",
  }

  file{ '/var/www/html/index.html':
    ensure   => present,
    content  => "Hello World!",
  }

  file { '/etc/nginx/sites-available/default.bk':
    ensure  => present,
    source  => File['/etc/nginx/sites-available/default']
  }
  file { '/etc/nginx/sites-available/default':
    ensure   => present,
    notify   => Service['nginx'],
    content  => $nginx_config,
  }

  service{ 'nginx':
    ensure   => running,
    enable   => true,
  }
}