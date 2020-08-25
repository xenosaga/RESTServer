from .user import user
from .admin import admin
from .scope import scope
from .command import command
from .account import account
from .. import room_map
from .. import admin_id
from .. import admin_cmd

adm = admin()
scope = scope()
cmd = command()
acct = account()

def query():
    pass

def delete():
    pass

def modify():
    pass

def add():
    pass


def process_group(post_data, scope, cmd_code):
    print(post_data)
    print(scope)
    print(cmd_code)
    
    # admin command
    if cmd_code[1] == 2:
        res = adm.process_key(post_data, cmd_code, scope)
        print(res)
    else:
        if adm.edit_mode() and adm.check_admin(uid):
            adm.process_value(post_data)
            pass

        else:

            pass
    
    # if(mag_cmd == True):
    #     res = adm.process(post_data, scope)
    #     print('admin mode init')
    #     return res
    # else:
    #     # admin commend
    #     print(adm.current_user)
    #     print(post_data['line_uid'])
    #     if(post_data['line_uid'] == adm.current_user):
    #         res = adm.process(post_data, scope)
    #         adm.clear_state()
    #         print('admin mode')
    #         return res
    #     # normal command
    #     else:
    #         print('user mode')
    #         print(post_data)
    #         prefix = 'nor'

    #         usr = user(prefix)
    #         res = usr.process(post_data, scope)
    #         return res

def process(post_data):
    res = {}

    # initial
    cmd_code = 0       #query code
    str_list = post_data['text'].split(" ")

    # check admin command
    cmd_code = cmd.check_command(str_list[0])
    print(cmd_code)

    priority = acct.check_priority(cmd_code, post_data['line_uid'])
    print(priority)
    
    if priority:
        # set scope
        scope_list = None
        if(post_data.get('group_id') != None):
            scope_list = scope.get_scope(post_data['group_id'])
            # print(scope_list)
            # only process group list
            res = process_group(post_data, scope_list, cmd_code)

        pass
    else :
        return res
        

    # elif(post_data.get('room_id') != None):
    #     pass


    # print('----------result-----------')
    # print(res)
    # print('---------------------------')
    # pass

