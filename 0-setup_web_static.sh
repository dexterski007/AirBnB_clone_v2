#!/usr/bin/env bash
#script to prepare for web static

sudo apt update
sudo apt -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html'
rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
if ! grep -q "location /hbnb_static" "/etc/nginx/sites-available/default"; then
	sudo sed -i '/root \/var\/www\/html/{;a location /hbnb_static {\n\talias \/data\/web_static\/current\/;\n\t}
}' /etc/nginx/sites-available/default
fi
sudo systemctl restart nginx
