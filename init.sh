#!/bin/sh

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/guni-dj.py /etc/gunicorn.d/guni-dj.py
sudo etc/init.d/gunicorn restart
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
