# Resets the Ulimit of the nginx server

exec { 'update-ulimit':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => 'usr/local/bin:/bin',
  notify  => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command     => 'service nginx restart',
  path        => ['/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  refreshonly => true,
}
