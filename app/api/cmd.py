from flask import jsonify, request
from . import api
from .. import db
from ..models import bbl_cmd_t

@api.route('/')
def no_perimision():
    res = {}
    res['code'] = 500
    res['msg'] = "no permission"
    
    return jsonify(res)
    
@api.route('/hello')
def hello():
    return jsonify({"Hello": "world"})
    

@api.route('/init')
def init():
    db.drop_all()
    db.create_all()
    db.session.commit()
    return 'OK'
 
@api.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()
    
    cmd_data = bbl_cmd_t(cmd_id=data['cmd'], cmd_rsp=data['rsp'], cmd_type=data['type'])
    db.session.add(cmd_data)
    db.session.commit()


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

    cmd_data = bbl_cmd_t.query.filter_by(cmd_id=data['cmd']).first()

    return jsonify(cmd_data)
