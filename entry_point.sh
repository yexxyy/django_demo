#!/bin/bash

#等待msyql就绪
./wait-for-it.sh $MYSQL_HOST:3306 &
wait

#应用启动前刷新数据库
python3.6 manage.py migrate --noinput

#加载管理员账号
python3.6 manage.py loaddata ./fixture/superuser.json

#收集静态文件
python3.6 manage.py collectstatic --noinput

#启动
uwsgi --ini uwsgi.ini