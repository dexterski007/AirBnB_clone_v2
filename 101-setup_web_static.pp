# puppet nginx server configurator

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file { [
  '/data/',
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/shared/',
  '/data/web_static/releases/test/',
]:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  recurse => true,
  force   => true,
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test/'],
  force   => true,
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
",
  require => Package['nginx'],
  force   => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "
server {
    listen 80 default_server;
    add_header X-Served-By $hostname;
    listen [::]:80 default_server;
    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    root /var/www/html;
    location /hbnb_static {
    alias /data/web_static/current/;
    }

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}
",
  notify  => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command   => '/bin/systemctl restart nginx',
  subscribe => [
  File['/etc/nginx/sites-available/default'],
  File['/data/web_static/releases/test/index.html'],
],
}
