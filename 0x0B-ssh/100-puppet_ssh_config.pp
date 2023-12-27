# configures ssh for connection to sever
$file_content = @("EOF")
IdentityFile ~/.ssh/school
PasswordAuthentication no
EOF

file { '/home/root/.ssh/config':
  ensure  => present,
  content => $file_content,
}
