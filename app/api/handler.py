from .parser import parser

from .. import db
from ..models import User, History

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
    h = History(line_uid=post_data['line_uid'], 
                line_group=post_data['line_group'],
                line_msg=post_data['text'])
    db.session.add(h)
    db.session.commit()    

    # get cmd code privilage
    [cmd_code, param, permission] = p.parse_text(post_data['text'])


    # check permission
    u = User()
    qu = u.query.filter_by(line_uid=post_data['line_uid'])
    
    # Write data mode(overwrite cmd_code)
    if( u.process_lock ):
        # image
        if( post_data['type'] == 0):
            cmd_code = 4
        # text
        elif( post_data['type'] == 1):
            cmd_code = 5
        # sticker
        elif( post_data['type'] == 2):
            cmd_code = 6 

    # 沒有權限
    if( not qu.can(permission) ):
        pass
    else :
        p.process_keyword(cmd_code, param, u.line_uid)
        pass

    
