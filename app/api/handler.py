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

# --------admin -----------
# addimg keyword [share]        2/3
# addtext keyword [share]       2/3
# --------user -------------
# query                         1
# in_op 12 title datetime       4
# in_del title                  2
# in_add_p title index          3
# in_del_p title index          3
# in_query [title/all]          2
def command_check(post_data):
    str_list = post_data['text'].split(" ")
    if(str_list[0] in admin_cmd):
        return True
    else:
        return False

def process_group(post_data, scope, mag_cmd):
    if(mag_cmd == True):
        res = adm.process(post_data, scope)
        print('admin mode init')
        return res
    else:
        # admin commend
        print(adm.current_user)
        print(post_data['line_uid'])
        if(post_data['line_uid'] == adm.current_user):
            res = adm.process(post_data, scope)
            adm.clear_state()
            print('admin mode')
            return res
        # normal command
        else:
            print('user mode')
            print(post_data)
            prefix = 'nor'

            usr = user(prefix)
            res = usr.process(post_data, scope)
            return res

def process(post_data):
    res = {}
    # initial

    mag_cmd = False
    # check admin command
    mag_cmd = command_check(post_data)
    
    # set scope
    scope = 'nor'
    if(post_data.get('group_id') != None):
        # only process group list
        if(post_data['group_id'] in room_map.keys()):
            scope = room_map[post_data['group_id']]
            res = process_group(post_data, scope, mag_cmd)
        

    elif(post_data.get('room_id') != None):
        pass


    print('----------result-----------')
    print(res)
    print('---------------------------')
    pass

