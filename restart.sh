#!/bin/sh
PWD= `pwd`
kill `cat ./manage.pid`

/usr/bin/python $PWD/manage.py runfcgi host=127.0.0.1 port=8027 pidfile=$PWD/manage.pid daemonize=true maxspare=1
