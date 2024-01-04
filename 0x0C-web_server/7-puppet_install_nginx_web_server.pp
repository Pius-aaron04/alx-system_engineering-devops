# Manifest Installs and configures Nginx Web server

CONFIG=@("EOF")
server{
    listen 80;
    server_name techsorce.tech;
    root /var/www/techsorce.tech/html;
    index /index.html;
    loaction /redirect_me{
        return 301 https://techsorce.tech$urirequest;
    }
}
EOF
class webserver::nginx{

  package{'nginx':
    ensure   => installed,
    provider => "apt",
  }

  file{ '/var/www/techsorce.tech/html/index.html':
    ensure => present,
    content => "Hello World!",
  }

  file { '/etc/nginx/sites-available/techsorce.tech':
    ensure  => present,
    notify  => Service['nginx'],
    content => $CONFIG,
    mode    => 755,
  }

  file { '/etc/nginx/sites-enabled/techsorce.tech':
    ensure   => link,
    target   => '/etc/nginx/sites-available/techsorce.tech',
    required => FILE['/etc/nginx/sites-available/techsorce.tech'],
    mode     => '755',
    user     => 'ubuntu',
    group    => 'ubuntu',
  }

  service{ 'nginx':
    ensure   => running,
    enable  => true,
  }
}