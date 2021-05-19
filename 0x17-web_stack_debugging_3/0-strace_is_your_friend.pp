# Find out why Apache is returning a 500 error
exec { 'fixit':
  command  => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
  provider => 'shell'
}
