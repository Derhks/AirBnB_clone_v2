# This script setup the servers for deploy a website
exec { 'apt-get update':
  command     => '/usr/bin/apt-get update',
}

exec { 'apt-get upgrade':
  command => '/usr/bin/apt-get -y upgrade',
  require => Exec['apt-get update'],
}

package { 'nginx':
  ensure   => 'latest',
  provider => 'apt',
  require  => Exec['apt-get upgrade'],
}

exec { 'create_folders':
  command => 'mkdir /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/',
  path    => '/bin',
  require => Package['nginx'],
}

exec { 'create_file':
  command => 'echo "AirBnb Clone Project is Running" > /data/web_static/releases/test/index.html',
  path    => '/bin',
  require => Exec['create_folders'],
}

exec { 'create_symlink':
  command => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  path    => '/bin',
  require => Exec['create_file'],
}

exec { 'change_owner':
  command => 'chown -R ubuntu:ubuntu /data/',
  path    => '/bin',
  require => Exec['create_symlink'],
}

exec { 'setup_nginx':
  command => 'sed -i "28 a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default',
  path    => '/bin',
  require => Exec['change_owner'],
}

exec { 'start_nginx':
  command => '/etc/init.d/nginx restart',
  require => Exec['setup_nginx'],
}
