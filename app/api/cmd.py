from flask import jsonify, request
from . import api
from .. import db
from ..chat_models import cmd_t, history_t
from .handler import process

@api.route('/', methods=['POST'])
def main_api():
    res = {}
    if(request.method == 'POST'):
        print('Post')
        req_data = request.json
        res = req_data
        process(req_data)
    return jsonify(res)
    
@api.route('/hello')
def hello():
    return jsonify({"Hello": "world"})
    

@api.route('/init', methods=['GET', 'POST'])
def init():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return 'OK'
 
@api.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    
    his_o = history_t('bbl')
    his_o.line_msg = data['cmd']
    his_o.line_uid = data['rsp']
    his_o.scope = data['scope']
    his_o.add()

    # cmd_o = cmd_t('bbl')
    # cmd_o.cmd_id = data['cmd']
    # cmd_o.cmd_rsp = data['rsp']
    # cmd_o.cmd_scope = data['scope']
    # cmd_o.cmd_type = data['type']
    # cmd_o.add()

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
