# Corrects the typo in a php file causing the 500 error


$file_path = '/var/www/html/wp-settings.php'
$old_string = 'class-wp-local.phpp'
$new_string = 'class-wp-local.php'

file { $file_path:
  ensure  => file,
  content => file($file_path, 'replace', "${old_string}" => "${new_string}"),
}
