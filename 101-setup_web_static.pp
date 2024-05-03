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
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
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
