#!/bin/sh

gunicorn manage:app --worker-class gevent --bind 127.0.0.1:5000

