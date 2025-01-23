# Puppet manifest for setting up the web server to deploy web_static:
# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
  require => Package['nginx'],
}

# Create the required directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
  recurse => true,
}

# Create a fake HTML file in the test release folder
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => "<html>
  <head>
  </head>
  <body>
      ALX
  </body>
</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create or update the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => File['/data/web_static/releases/test/index.html'],
}

# Update Nginx configuration to serve /data/web_static/current to hbnb_static
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Restart Nginx service to apply changes
exec { 'restart_nginx':
  command     => '/bin/systemctl restart nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}