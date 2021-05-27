# User limit
exec { 'fixithard':
  command  => 'sed -i s/holberton hard nofile 5/holberton hard nofile 550000/g /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}

exec { 'fixitsoft':
  command  => 'sed -i s/holberton soft nofile 4/holberton soft nofile 550000/g /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}
