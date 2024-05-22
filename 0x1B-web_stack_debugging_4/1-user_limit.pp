# Resets the open files Ulimit for holberton

exec { 'update-ulimit':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 4096/' /etc/security/limits.conf",
  path    => 'usr/local/bin:/bin',
}

exec { 'update-ulimit-soft':
  command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 4096/' /etc/security/limits.conf",
  path    => 'usr/local/bin:/bin',
}
