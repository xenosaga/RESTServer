from flask import jsonify, request
from . import api
from .. import db
from ..bbl_models import bbl_cmd_t, bbl_history_t
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
    
    his_o = bbl_history_t()
    his_o.line_msg = data['cmd']
    his_o.line_uid = data['rsp']
    his_o.add()

    # cmd_data = bbl_cmd_t(cmd_id=data['cmd'], cmd_rsp=data['rsp'], cmd_type=data['type'])
    # db.session.add(cmd_data)
    # db.session.commit()


    return jsonify(data)

@api.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()

    cmd_data = bbl_cmd_t.query.filter_by(cmd_id=data['cmd']).first()
    db.session.delete(cmd_data)
    db.session.commit()

    return jsonify(data)

@api.route('/query', methods=['POST'])
def query():
    data = request.get_json()

    his_data = bbl_history_t(line_msg='', line_uid='')
    row_data = his_data.get_all_message()
    for obj in row_data:
        print(obj.line_msg)

    return 'OK'
