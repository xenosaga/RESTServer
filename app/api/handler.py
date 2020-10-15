from .parser import parser

from .. import db
from ..models import Role, User, History
from .utilty import reset_response
from .emu import UserLockType

p = parser()

# cmd           code
# ------------------------
# query         0
# addimg        1
# addtext       2
# addsticker    3
# modimg        4
# modtext       5
# modsticker    6
# deleteimg     7
# delete        8
# guild         10
# inst_op       11
# inst_del      12
# inst_add_p    13
# inst_del_p    14
# inst_query    15

def process(post_data):
    res = {}

    # write log
    h = History(line_uid=post_data['src_uid'], 
                src_gid=post_data['src_gid'],
                src_type=post_data['src_type'],
                line_msg=post_data['msg_text'])
    db.session.add(h)
    db.session.commit()    

    # get cmd code privilage
    [cmd_code, param, permission] = p.parse_text(post_data['msg_text'])

    print('cmd_code: ', cmd_code)
    print('param: ', param)
    print('permission: ', permission)

    # check permission
    qu = User.query.filter_by(line_uid=post_data['src_uid']).first()
    
    print('--------------------')  
    if qu is None:
        role = Role.query.filter_by(default=True).first()
        print('permission: ', role.permission)

        # add user
        u = User()
        u.line_id = ''
        u.line_uid = post_data['src_uid']
        u.role_id = role.permission
        u.process_lock = False
        u.last_word = ''

        db.session.add(u)
        db.session.commit()
        print(u.role_id)
        return res

    # Write data mode(overwrite cmd_code)
    if( qu.process_lock ):
        # image
        if( qu.lock_type == UserLockType.IMG_LOCK):
            cmd_code = 4
        # text
        elif( qu.lock_type == UserLockType.TEXT_LOCK):
            param[0] = post_data['msg_id']
            cmd_code = 5
        # sticker
        elif( qu.lock_type == UserLockType.STICKER_LOCK):
            cmd_code = 6 

    # 沒有權限
    if( not qu.can(permission) ):
        print('no premission')
        reset_response(res)
        pass
    else :
        print('process')
        res = p.process_keyword(cmd_code, param, qu.line_uid, 
            post_data['msg_id'], post_data['msg_sid'], post_data['msg_pid'])
        print(res)
        pass
    
    return res

# post back data
def process_pb(post_data):
    print('post back')
    p.process_pb(post_data['data'], post_data['params'])
