#!/usr/bin/env bash
#script to prepare for web static

sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /var/www/html/data/
sudo mkdir -p /var/www/html/data/web_static/releases/test/
sudo mkdir -p /var/www/html/data/web_static/shared/
sudo sh -c 'echo "Hello World!" > /var/www/html/data/web_static/releases/test/index.html'
sudo ln -fs /var/www/html/data/web_static/current /var/www/html/data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /var/www/html/data/
if ! grep -q "location hbnb_static" "/etc/nginx/sites-available/default"; then
	sudo sed -i '/root \/var\/www\/html/{;a \
    location hbnb_static {\n\talias \/var\/www\/html\/data\/web_static\/current\/;\n\t}
}' /etc/nginx/sites-available/default
fi
sudo systemctl restart nginx
