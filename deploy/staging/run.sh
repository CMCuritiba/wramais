#!/usr/bin/env bash

#source /usr/share/envs/wramais/bin/activate

cd /usr/share/webapps/wramais

exec /usr/share/envs/wramais/bin/gunicorn config.wsgi -c deploy/staging/gunicorn.conf.py  --env DJANGO_SETTINGS_MODULE=config.settings.production