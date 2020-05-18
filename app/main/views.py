from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return '<h1>Main page</h1>'

@main.route('/upload', methods=['GET'])
def upload():
    # return 'OK'
    return render_template('index.html')

@main.route('/upload_handle', methods=['POST'])
def upload_handle():
    print('-----------------------------------\n')
    print(request.form)
    print('-----------------------------------\n')
    # return 'OK'
    return redirect(url_for('main.upload'))

@main.route('/instance', methods=['GET'])
def instance():
    return render_template('instance.html')