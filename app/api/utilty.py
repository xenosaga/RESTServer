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
    res['msg_text'] = 'input text'

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
    res['msg_text'] = 'input image'

    print(res)
    return res

def AddSticker(line_uid, param):
    print('add sticker')
    res = {}
    reset_response(res)

    print(param)

    u = User.query.filter_by(line_uid=line_uid).first()
    u.last_word = param[1]
    u.process_lock = True
    u.lock_type = 3
    db.session.add(u)
    db.session.commit()

    res['type'] = 1
    res['msg_text'] = 'input sticker'
    return res

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
            res['msg_descr'] = r.keyword
        elif (r.rtype == 3):
            res['pid'] = r.package
            res['sid'] = r.stick

    print('result is ')
    print(res)
    return res

def Delete(param):
    print('delete')

    res = {}
    reset_response(res)

    gd = Gdata.query.filter_by(keyword=param[1]).first()
    if((not gd is None) and (gd.rtype != 2)):
        db.session.delete(gd)
        db.session.commit()
        res['type'] = 1
        res['msg_text'] = 'delete ' + param[1]
    else:
        res['type'] = 1
        res['msg_text'] = 'nothing to do'
    
    return res
    
def DeleteImg(param):
    print('delete image')

    res = {}
    reset_response(res)

    gd = Gdata.query.filter_by(keyword=param[1]).first()
    if((not gd is None) and (gd.rtype is 2)):
        url = gd.response
        # delete from imgurl

        db.session.delete(gd)
        db.session.commit()
        res['type'] = 1
        res['msg_text'] = 'delete image : ' + param[1]
    else:
        res['type'] = 1
        res['msg_text'] = 'nothing to do'

    return res

def ModImg(line_uid, msg_id):
    print('modify image')

    res = {}
    reset_response(res)

    # clean flag 
    u = User.query.filter_by(line_uid=line_uid).first()
    u.process_lock = False
    db.session.add(u)
    db.session.commit()

    gd = Gdata()
    gd.keyword = u.last_word
    gd.response = msg_id
    gd.stick = 0
    gd.package = 0
    gd.rtype = 2
    db.session.add(gd)
    db.session.commit()
    
    res['type'] = 1
    res['msg_text'] = 'img update finished'
    return res
    
def ModText(line_uid, param):
    print('modify text')
    
    res = {}
    reset_response(res)

    # clean flag 
    u = User.query.filter_by(line_uid=line_uid).first()
    u.process_lock = False
    db.session.add(u)
    db.session.commit()

    gd = Gdata()
    gd.keyword = u.last_word
    gd.response = param[0]
    gd.stick = 0
    gd.package = 0
    gd.rtype = 1
    db.session.add(gd)
    db.session.commit()

    res['type'] = 1
    res['msg_text'] = 'text update finished'
    
    return res
    
def ModSticker(line_uid, sid, pid):
    print('modify sticker')

    res = {}
    reset_response(res)

    # clean flag 
    u = User.query.filter_by(line_uid=line_uid).first()
    u.process_lock = False
    db.session.add(u)
    db.session.commit()

    gd = Gdata()
    gd.keyword = u.last_word
    gd.response = ''
    gd.stick = sid
    gd.package = pid
    gd.rtype = 3
    db.session.add(gd)
    db.session.commit()
    
    res['type'] = 1
    res['msg_text'] = 'sticker update finished'
    
    return res

def Guild(param):
    print('guild')

    res = {}
    reset_response(res)

    pass

def InstOpen(param):
    print('Inst open')

    pass

def InstDelete(param):
    print('Inst delete')

    pass

def InstAddPlayer(param):
    print('Inst add player')

    pass

def InstDelPlayer(param):
    print('Inst del player')

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