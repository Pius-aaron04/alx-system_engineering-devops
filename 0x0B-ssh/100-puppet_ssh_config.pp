# configures ssh for connection to sever
$file_content = @("EOF")
IdentityFile ~/.ssh/school
PasswordAuthentication no
EOF

file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => $file_content,
}
