# Installs flask package using pip3

package{ 'python3':
  ensure   => installed,
}

package{ 'python3-pip':
  ensure   => installed,
}

package{ 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
}

package{ 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}
