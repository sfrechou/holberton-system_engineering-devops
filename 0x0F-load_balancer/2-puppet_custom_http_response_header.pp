# Install nginx
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  name     => 'nginx',
}

::nginx::resource::vhost {
[...]
add_header=> {
'X-Served-By' => '$HOSTNAME',
}
}

service { 'nginx':
  ensure  => 'running',
}
