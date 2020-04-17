#!/usr/bin/env python
import os
from app import create_app, db
from app.models import cmd_t

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()
