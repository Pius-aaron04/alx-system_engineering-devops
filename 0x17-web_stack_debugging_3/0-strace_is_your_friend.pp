# Corrects the typo in a php file causing the 500 error


$file_path = '/var/www/html/wp-settings.php'

exec { $file_path:
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin', '/usr/bin']
}
