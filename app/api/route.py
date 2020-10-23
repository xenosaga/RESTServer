from flask import jsonify, request, render_template
from . import api
from .. import db
from .handler import process, process_pb
from ..models import Command, Role, User, Guild
from flask_cors import cross_origin

# Line api process
@api.route('/', methods=['POST'])
def main_api():
    res = {}
    if(request.method == 'POST'):
        print('Post')
        req_data = request.json
        res =   process(req_data)
    return jsonify(res)
    
@api.route('/postback', methods=['POST', 'GET'])
def post_back():
    if(request.method == 'POST'):
        print('post back')
        req_data = request.json
        res = process_pb(req_data)
    pass

@api.route('/hello', methods=['POST', 'GET'])
@cross_origin()
def hello():
    return jsonify({"Hello": "world"})

@api.route('/message', methods=['POST', 'GET'])
@cross_origin()
def get_message():
    res = [
        {
            'user': 'user1',
            'msg': 'hello'
        },
        {
            'user': 'user2',
            'msg': 'hi'
        },
        {
            'user': 'user1',
            'msg': 'I am user1'
        },
        {
            'user': 'user2',
            'msg': 'Hi user1'
        },
    ]
    return jsonify(res)

@api.route('/init', methods=['GET', 'POST'])
def init():
    db.drop_all()
    db.create_all()
    db.session.commit()
    Command.insert_commands()
    Role.insert_roles()
    User.init_testUser()
    Guild.init_testMember()
    return 'OK'
 
@api.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    
    his_o = history_t('bbl')
    his_o.line_msg = data['cmd']
    his_o.line_uid = data['rsp']
    his_o.scope = data['scope']
    his_o.add()

    return jsonify(data)

@api.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()

    cmd_data = cmd_t.query.filter_by(cmd_id=data['cmd']).first()
    db.session.delete(cmd_data)
    db.session.commit()

    return jsonify(data)

@api.route('/query', methods=['POST'])
def query():
    data = request.get_json()

    his_data = history_t('bbl')
    # row_data = his_data.get_all_message()
    row_data = his_data.get_msgs_by_scope(data['scope'])
    for obj in row_data:
        print(obj.line_msg)

    return 'OK'
