# Install nginx
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  name     => 'nginx',
}

location /etc/nginx/sites-available/default {
  add_header X-Served-B $HOSTNAME,      
}

service { 'nginx':
  ensure  => 'running',
}
