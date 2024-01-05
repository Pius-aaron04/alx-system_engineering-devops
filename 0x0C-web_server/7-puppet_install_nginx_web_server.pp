# Manifest Installs and configures Nginx Web server

$nginx_config=@(EOF)
server{
    listen 80 default_server;
    index /index.html;
    rewrite ^/redirect_me https://github.com/pius-aaron04 permanent;
    error_page 404 /404.html;
    location = /404.html{
        root /var/www/html/404.html;
        internal;
    }
}
EOF
class webserver::nginx{

  package{'nginx':
    ensure   => installed,
    provider => 'apt',
  }

  file{ '/var/www/html/index.html':
    ensure   => present,
    content  => 'Hello World!',
  }

  file { '/var/www/html/404.html':
    ensure   => present,
    content  => "Ceci n'est pas une page"
  }

  file { '/etc/nginx/sites-available/default.bk':
    ensure  => present,
    source  => File['/etc/nginx/sites-available/default']
  }

  file { '/etc/nginx/sites-available/default':
    ensure   => present,
    notify   => Service['nginx'],
    mode     => '644',
    content  => "$nginx_config",
  }

  service{ 'nginx':
    ensure   => running,
    enable   => true,
  }
}