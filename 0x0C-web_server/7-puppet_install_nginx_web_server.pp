# Install nginx
package { 'nginx':
  ensure   => present,
  name     => 'nginx',
  provider => 'apt',
}
# root / with a GET request using curl, it must return a page that contains the string Holberton School
file { 'index.html':
  path    => '/var/www/html/index.html',
  content => 'Holberton School',
}

# The redirection must be a “301 Moved Permanently”
file_line { '/redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;'
  line   => 'rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => 'running',
}