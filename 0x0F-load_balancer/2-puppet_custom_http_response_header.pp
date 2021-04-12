# Install nginx
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  name     => 'nginx',
}

exec {'Barney':
  command  => 'sudo apt-get -y update; sudo apt-get -y install nginx;
               sudo ufw allow 'Nginx HTTP';
               sudo sed -i "46i\ add_header X-Served-By $HOSTNAME ;" /etc/nginx/sites-available/default;
               sudo service nginx restart',
  provider => 'shell',

}

service { 'nginx':
  ensure  => 'running',
}
