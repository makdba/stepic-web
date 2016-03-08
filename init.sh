#!/bin/sh

sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/guni-dj.py /etc/gunicorn.d/guni-dj.py
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#step 2.11. Run gunicorn -b 0.0.0.0:8000 ask.wsgi from /web/ask 
