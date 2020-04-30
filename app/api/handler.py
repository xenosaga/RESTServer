from .user import user
from .admin import admin
from .. import room_map
from .. import admin_id
from .. import admin_cmd

adm = admin()

def query():
    pass

def delete():
    pass

def modify():
    pass

def add():
    pass

def process(post_data):
    res = {}
    # initial
    if(adm.line_uid == ''):
        if(post_data['text'] in admin_cmd):
            adm.line_id = post_data['line_uid']
            res = adm.process(post_data)
            print('admin mode init')
    else:
        # admin commend
        if(post_data['usr_id'] == adm.line_uid):
            res = adm.process(post_data)
            print('admin mode')
        # normal command
        else:
            print('user mode')
            print(post_data)
            prefix = 'nor'

            if(post_data['group_id'] in room_map.keys()):
                prefix = room_map[post_data['group_id']]

            usr = user(prefix)
            res = usr.process(post_data)

    print('----------result-----------')
    print(res)
    print('---------------------------')
    pass

