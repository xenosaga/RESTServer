
from .. import db
from ..chat_models import \
    cmd_t, history_t, guild_t, instance_t
import re

# state less object
class admin:

    def __init__(self):
        self.current_user = ''
        
        self.interactive = False
        self.proce_type = 'text'

        self.key = ''
        self.value = ''
        self.scope = ['bbl']
        self.type = 1
        self.init = False
        self.res_data = {'msg': 'no premission',
                         'type': 0
                        }
        self.admin_cmd = ['addimg', 'addtext']

    def check_command(self, text):
        return text in self.admin_cmd

    # proce_data
    #   line_uid
    #   text
    # res_data
    #   msg
    #   type
    def process(self, proc_data, scope):

        print(self.current_user)
        print(proc_data['line_uid'])

        # system guard
        if(self.current_user == ''):
            self.current_user = proc_data['line_uid']
            self.res_data['msg'] = 'input data'
            self.res_data['type'] = 1

        # 同一時間只有一個人管理 
        if(self.current_user != proc_data['line_uid']):
            print('invalid user')
            self.res_data['msg'] = 'Invalid user'
            self.res_data['type'] = 1
            return self.res_data
        
        if(proc_data['group_id'] != None):
            self.process_group(proc_data, scope)
            
        elif (proc_data['room_id'] != None):
            self.process_room(proc_data, scope)

        return self.res_data

    def process_room(self, proc_data):
        pass

    # addimg [all]
    # keyword
    # <image>
    def process_group(self, proc_data, scope):
        # default single line mode
        str_list = proc_data['text'].split(" ")
        
        print(str_list)
        # mod scope ( for initial )
        if(not self.init and len(str_list) == 3):
            if(str_list[2] == 'share'):
                self.scope = [scope, 'shr']
            else:
                self.scope = [scope]
            self.init = True

        # command and keyword
        if(str_list[0] == 'addimg'):
            self.proce_type = 'image'
            self.type = 2
            self.key = str_list[1]
        elif(str_list[0] == 'addtext'):
            self.proce_type = 'text'
            self.type = 1
            self.key = str_list[1]
        # value save data
        else:
            print('save value')
            if(self.type == 1):
                self.write_text(proc_data['text'])
            elif(self.type == 2):
                self.write_image(proc_data['text'])
                
    def write_db(self):
        print('---------- write db -----------')
        print(self.scope)

        cmd_table = cmd_t(self.scope[0])
        cmd_table.cmd_key = self.key
        cmd_table.cmd_rsp = self.value
        cmd_table.cmd_scope = self.scope[0]
        cmd_table.cmd_type = self.type

        # share command
        if(len(self.scope) > 1):
            cmd_table.cmd_scope = 'shr'
            res = cmd_table.get_cmds_by_key(cmd_key=self.key)
        else:
            res = cmd_table.get_cmd(cmd_key=self.key, scope=self.scope)
        
        print(res)
        
        # delete others 
        if(res != [] or res != None):
            for item in res :
                item.delete()
        # add record
        cmd_table.add()

    def write_image(self, value):
        # download image from line
        # upload image to imgur
        self.value = "url to imgur"
        self.write_db()
        self.res_data['msg'] = 'img saved'
        self.res_data['type'] = 1

    def write_text(self, value):
        self.value = value
        self.write_db()
        self.res_data['msg'] = 'text saved'
        self.res_data['type'] = 1

    def clear_state(self):
        self.current_user = ''
        self.init = False