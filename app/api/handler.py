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


def process_group(post_data, scope, cmd_code, cmd_list):
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


def process(post_data):
    res = {}

    # get scope
    scope = scope.get_scope(post_data['group_id'])

    # get user privilege
    usr_priv = user.get_user_privilege(post_data['line_uid'], post_data['group_id'])

    # get cmd code privilage
    [cmd_code, param] = cmd.get_cmd_code(post_data['text'])

    
    # # initial
    # cmd_code = 0       #query code
    # cmd_list = post_data['text'].split(" ")

    # # check admin command
    # cmd_code = cmd.check_command(cmd_list[0])
    # print(cmd_code)

    # priority = acct.check_priority(cmd_code, post_data['line_uid'])
    # print(priority)
    
    # if priority:
    #     # set scope
    #     scope_list = None
    #     if(post_data.get('group_id') != None):
    #         scope_list = scope.get_scope(post_data['group_id'])
    #         # print(scope_list)
    #         # only process group list
    #         res = process_group(post_data, scope_list, cmd_code, cmd_lsit)

    #     pass
    # else :
    #     return res

