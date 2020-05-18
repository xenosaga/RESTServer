from .user import user
from .admin import admin
from .scope import scope
from .command import command
from .. import room_map
from .. import admin_id
from .. import admin_cmd

adm = admin()
scope = scope()
cmd = command()

def query():
    pass

def delete():
    pass

def modify():
    pass

def add():
    pass


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

    cmd_code = 0       #query code
    str_list = post_data['text'].split(" ")

    # check admin command
    cmd_code = cmd.check_command(str_list[0])
    print(cmd_code)
    
    # set scope
    # scope = 'nor'
    # if(post_data.get('group_id') != None):
    #     # only process group list
    #     if(post_data['group_id'] in room_map.keys()):
    #         scope = room_map[post_data['group_id']]
    #         res = process_group(post_data, scope, mag_cmd)
        

    # elif(post_data.get('room_id') != None):
    #     pass


    # print('----------result-----------')
    # print(res)
    # print('---------------------------')
    # pass

