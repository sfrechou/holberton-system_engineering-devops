# Find out why Apache is returning a 500 error
exec { 'fixit':
  command  => 'sudo sed -i "80i\ define('WP_DEBUG', true);" /var/www/html/wp-config.php';
  provider => 'shell',
}
