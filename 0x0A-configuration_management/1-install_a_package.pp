# Installs flask package using pip3

package{ 'flask':
  ensure   => installed,
  name     => 'flask',
  provider => 'pip3',
}
