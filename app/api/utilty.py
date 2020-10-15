from .. import db
from ..models import Gdata, Gplayer, Guild, User, Instence
from .emu import UserLockType, RspDataType
from flask import jsonify
from .message import GetTimeMenu

def AddText(line_uid, param):
    print('addtext')
    res = {}
    reset_response(res)

    print(param)
    # update lock
    u = User.query.filter_by(line_uid=line_uid).first()
    u.last_word = param[1]
    u.process_lock = True
    u.lock_type = UserLockType.TEXT_LOCK
    db.session.add(u)
    db.session.commit()

    res['type'] = RspDataType.TEXT
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
    u.lock_type = UserLockType.IMG_LOCK
    db.session.add(u)
    db.session.commit()

    res['type'] = RspDataType.TEXT
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
    u.lock_type = UserLockType.STICKER_LOCK
    db.session.add(u)
    db.session.commit()

    res['type'] = RspDataType.TEXT
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

    # 有找到東西
    if(not r is None):
        print(r.rtype)
        res['type'] = r.rtype
        
        if(r.rtype == RspDataType.TEXT):
            res['msg_text'] = r.response
        elif (r.rtype == RspDataType.IMG):
            res['url_origin'] = r.response
            res['url_preview'] = r.response
            res['msg_descr'] = r.keyword
        elif (r.rtype == RspDataType.STICKER):
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
        res['type'] = RspDataType.TEXT
        res['msg_text'] = 'delete ' + param[1]
    else:
        res['type'] = RspDataType.TEXT
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
        res['type'] = RspDataType.TEXT
        res['msg_text'] = 'delete image : ' + param[1]
    else:
        res['type'] = RspDataType.TEXT
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
    
    res['type'] = RspDataType.TEXT
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

    res['type'] = RspDataType.TEXT
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
    
    res['type'] = RspDataType.TEXT
    res['msg_text'] = 'sticker update finished'
    
    return res

def GuildList():
    print('guild')

    res = {}
    reset_response(res)

    mbrs = Guild.query.filter_by(guild_name='bbl').all()
    
    rows = []
    for m in mbrs:
        row = [m.game_id, m.line_id, m.game_job]
        rows.append(row)

    res['type'] = RspDataType.FLEX
    res['msg_flex'] = rows

    return res

def InstOpen(line_uid, param):
    print('Inst open')
    
    res = {}
    reset_response(res)

    # check if has in database
    ins = Instence.query.filter_by(title=param[1]).first()
    if (ins is not None) :
        res['type'] = RspDataType.TEXT
        res['msg_text'] = 'already this title'
        return res

    # Lock state
    u = User.query.filter_by(line_uid=line_uid).first()
    u.process_lock = True
    u.lock_type = UserLockType.INST_LOCK
    u.last_word = param[1]
    db.session.add(u)
    db.session.commit()

    # Insert instence
    ins = Instence()
    ins.title = param[1]
    ins.game_type = param[2]
    ins.create_user = line_uid
    ins.max_player = 6
    if( param[2] == '12'):
        ins.max_player = 12
    ins.cur_palyer = 0
    db.session.add(ins)
    db.session.commit()

    # create time menu
    TimeMenu = GetTimeMenu(ins.title)

    res['type'] = RspDataType.FLEX
    res['msg_flex'] = TimeMenu

    return res

def InstDelete(line_uid, param):
    print('Inst delete')

    res = {}
    reset_response(res)

    u = User.query.filter_by(line_uid=line_uid).first()
    u.process_lock = False
    u.lock_type = UserLockType.UNLOCK
    db.session.add(u)
    db.session.commit()

    ins = Instence.query.filter_by(title=param[1]).first()
    if( line_uid == ins.create_user ):
        db.session.delete(ins)
        db.session.commit()
        res['type'] = RspDataType.TEXT
        res['msg_text'] = param[1] + " is deleted "

    res['type'] = RspDataType.FLEX
    res['msg_flex'] = rows

    return res

def InstQuery():
    print('Inst query')

    res = {}
    reset_response(res)

    ins = Instence.query.all()

    rows = []
    for i in ins:
        row = [i.title, i.game_type, i.date_time, i.cur_palyer]
        rows.append(row)

    res['type'] = RspDataType.FLEX
    res['msg_flex'] = rows

    return res

def InstAddPlayer(line_uid, param):
    print('Inst add player')

    res = {}
    reset_response(res)

    # check user
    u = User.query.filter_by(line_uid=line_uid).first()
    if( u is None):
        res['type'] = RspDataType.TEXT
        res['msg_text'] = 'No such user'
        return res

    # chexk instance
    ins = Instence.query.filter_by(title=param[1]).first()
    if( ins is None):
        res['type'] = RspDataType.TEXT
        res['msg_text'] = 'No such title'
        return res

    # check has been list
    gp = Gplayer.query.filter_by(line_uid=line_uid, 
                                 inst_title=param[1], 
                                 game_id=param[2]).first()
    if (gp is None) :
        gp = Gplayer()
        gp.inst_title = param[1]
        gp.game_id = param[2]
        gp.line_uid = line_uid
        gp.team_id = 1
        if( ins.max_player == 12 and ins.cur_palyer >= 6):
            gp.team_id = 2
        
        if( ins.cur_palyer >= ins.max_player) :
            res['tyep'] = RspDataType.TEXT
            res['msg_text'] = 'Team is full'
            return res
        else :
            # update current player
            ins.cur_palyer = ins.cur_palyer + 1
            db.session.add(ins)
            db.session.commit()

            db.session.add(gp)
            db.session.commit()

            res['type'] = RspDataType.TEXT
            res['msg_text'] = 'add player successed'

    return res

def InstDelPlayer(line_uid, param):
    print('Inst del player')

    res = {}
    reset_response(res)

    # check instence
    ins = Instence.query.filter_by(title=param[1]).first()
    if( ins is None):
        res['type'] = RspDataType.TEXT
        res['msg_text'] = 'No such instance'
        return res

    gp = Gplayer.query.filter_by(
            inst_title=param[1], 
            game_id=param[2]).first()
    
    if( gp is not None) :
        if( gp.line_uid == line_uid or ins.create_user == line_uid):
            db.session.delete(gp)
            db.session.commit()

            ins.cur_palyer = ins.cur_palyer - 1
            db.session.add(ins)
            db.session.commit()

            res['type'] = RspDataType.TEXT
            res['msg_text'] = 'delete ' + param[2]

    return res

def PostbackInst(title, datetime):
    
    ins = Instence.query.filter_by(title=title).first()
    if(ins is not None):
        ins.date_time = datetime
        db.session.add(ins)
        db.session.commit()
        
    pass

def reset_response(res):
    res['type'] = RspDataType.SILENT
    res['msg_text'] = ''
    res['msg_descr'] = ''
    res['msg_alter'] = ''
    res['msg_flex'] = ''
    res['url_origin'] = ''
    res['url_preview'] = ''
    res['sid'] = 0
    res['pid'] = 0