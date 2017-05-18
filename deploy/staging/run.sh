#!/usr/bin/env bash

cd /usr/share/webapps/wramais

exec /usr/share/envs/wramais/bin/gunicorn wramais/config/wsgi.py -c deploy/staging/gunicorn.conf.py  