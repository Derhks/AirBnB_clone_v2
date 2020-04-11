#!/usr/bin/env bash
# Installing nginx and setup to serve the content
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo apt-get update
# Create folder and files
mkdir /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
echo "AirBnb Clone Project is Running" > /data/web_static/releases/test/index.html
# Create a symlink
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Change the own of a folder
chown -R ubuntu:ubuntu /data/
# Setup nginx to serve the content
location="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "28 a $location" /etc/nginx/sites-enabled/default
# Start nginx
sudo service nginx restart
