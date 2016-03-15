#!/bin/sh

#MySQL initial actions
mysql -uroot -e"CREATE DATABASE webdb"
mysql -uroot -e"CREATE USER 'webdbuser'@'localhost' IDENTIFIED BY 'webdb'"
mysql -uroot -e"GRANT ALL ON webdb.* TO 'webdbuser'@'localhost'"
mysql -uroot -e"FLUSH PRIVELEGES;"
 
