from datetime import datetime
from flask import render_template, session, redirect, url_for, request

from . import main
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
    # return '<h1>Main page</h1>'

@main.route('/test', methods=['GET', 'POST'])
def test():
    data = request.json
    print(data['name'])
    print(data['msg'])
    return 'OK'
    # return render_template('test.html')

@main.route('/upload', methods=['GET'])
def upload():
    # return 'OK'
    return render_template('upload.html')

@main.route('/instance/open', methods=['GET'])
def instance_open():
    return render_template('instance_open.html')

@main.route('/instance/list', methods=['GET'])
def instance_list():
    return render_template('instance_list.html')

@main.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@main.route('/chat', methods=['GET'])
def chat():
    messages = [
        {
            'name':'user1',
            'message':'message1'
        },
        {
            'name':'user1',
            'message':'message2'

        },
        {
            'name':'user2',
            'message':'message3'
        },
        {
            'name':'user2',
            'message':'message3'
        }
    ]
    
    return render_template('chat.html', msgs=messages)

@main.route('/upload_handle', methods=['POST'])
def upload_handle():
    print('-----------------------------------\n')
    print(request.form)
    print('-----------------------------------\n')
    # return 'OK'
    return redirect(url_for('main.upload'))

@main.route('/instance_handle', methods=['POST'])
def instance_handle():
    print('-----------------------------------\n')
    print(request.form)
    print('-----------------------------------\n')
    return redirect(url_for('main.instance_open'))