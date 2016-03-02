#!/bin/sh

rm /etc/nginx/sites-eanbled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enables/default
sudo /etc/init.d/nginx restart
