from flask import jsonify, request
from . import api
from .. import db
from ..models import cmd_t

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
 
@api.route('/insert/<key>/<val>/<ctype>')
def insert(key, val, ctype):
    cmd_data = cmd_t(cmd_id=key, cmd_rsp=val, cmd_type=ctype)
    db.session.add(cmd_data)
    db.session.commit()
    return 'OK'
