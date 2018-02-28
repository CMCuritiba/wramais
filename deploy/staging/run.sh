#!/usr/bin/env bash

#source /usr/share/envs/wramais/bin/activate

cd /usr/share/webapps/wramais

mkdir -p /usr/share/webapps/wramais/var/run
rm -f /usr/share/webapps/wramais/var/run/*

exec /usr/share/envs/wramais/bin/gunicorn config.wsgi -c deploy/staging/gunicorn.conf.py  --env DJANGO_SETTINGS_MODULE=config.settings.production