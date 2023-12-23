# creates file 'school' in tmp dir

file {'/tmp/school':
	path => '/tmp/school',
     ensure => present,
     mode => '0744',
     owner => 'www-data',
     group => 'www-data',
     content => 'I love Puppet',
     target => '/tmp/school'
}
