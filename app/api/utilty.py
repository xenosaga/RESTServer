from .. import db
from ..models import Gdata, Gplayer, Guild, User, Instence

def AddText(line_uid, param):
    print('addtext')
    res = {}
    reset_response(res)

    print(param)
    # update lock
    u = User.query.filter_by(line_uid=line_uid).first()
    u.last_word = param[1]
    u.process_lock = True
    u.lock_type = 1
    db.session.add(u)
    db.session.commit()

    res['type'] = 1
    res['msg_text'] = 'input data'

    return res
    pass

def AddImg(line_uid, param):
    print('addimg')
    res = {}
    reset_response(res)

    print(param)

    u = User.query.filter_by(line_uid=line_uid).first()
    u.last_word = param[1]
    u.process_lock = True
    u.lock_type = 2
    db.session.add(u)
    db.session.commit()

    res['type'] = 1
    res['msg_text'] = 'input data'

    return res
    pass

def AddSticker(line_uid, param):
    pass

# query command
# eg
# 神諭
def Query(param):
    print("Query")

    res = {}
    reset_response(res)
    qstring = param[0]
    print('qstring: ', qstring)
    r = Gdata.query.filter_by(keyword=qstring).first()

    print(r.rtype)
    # 有找到東西
    if(not r is None):
        res['type'] = r.rtype
        
        if(r.rtype == 1):
            res['msg_text'] = r.response
        elif (r.rtype == 2):
            res['url_origin'] = r.response
            res['url_preview'] = r.response
        elif (r.rtype == 3):
            res['pid'] = r.package
            res['sid'] = r.sticker

    print('result is ')
    print(res)
    return res

def Delete(param):
    pass

def DeleteImg(param):
    pass

def ModImg(line_uid, param):
    print('modify image')

    res = {}
    reset_response(res)

    # clean flag 
    u = User.query.filter_by(line_uid=line_uid).first()
    u.process_lock = 0
    db.session.add(u)
    db.session.commit()

    gd = Gdata()
    gd.keyword = u.last_word
    gd.response = param[0]
    gd.stick = 0
    gd.package = 0
    gd.rtype = 2
    db.session.add(gd)
    db.session.commit()
    
    pass

def ModText(line_uid, param):
    pass

def ModSticker(line_uid, param):
    pass

def reset_response(res):
    res['type'] = 0
    res['msg_text'] = ''
    res['msg_descr'] = ''
    res['msg_alter'] = ''
    res['msg_flex'] = ''
    res['url_origin'] = ''
    res['url_preview'] = ''
    res['sid'] = 0
    res['pid'] = 0