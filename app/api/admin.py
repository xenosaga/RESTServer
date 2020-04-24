
from .. import db
from ..moe_models import moe_cmd_t, moe_history_t, moe_guild_t, moe_instance_t
from ..bbl_models import bbl_cmd_t, bbl_history_t, bbl_guild_t, bbl_instance_t
import re

# state less object
class admin:

    def __init__(self):
        self.line_id = ''
        self.query = ''
        self.res = ''
        self.current_user = ''
        self.step = 0
        self.bbl_cmd_t = bbl_guild_t()
        self.bbl_guild_t = bbl_guild_t()
        
        self.bbl_cmd_t = moe_guild_t()
        self.bbl_instance_t = moe_instance_t()
    
        self.interactive = False
        self.proce_type = 'text'
        self.group = 'bbl'

        self.key = ''
        self.value = ''
        self.type = 1
        self.res_data = {'msg': 'no premission',
                         'type': 0
                        }
        self.addimg = re.compile('addimg')
        self.addtext = re.compile('addtext')
        self.guild = re.compile('guild')
        self.delete = re.compile('delete')

    # proce_data
    #   line_uid
    #   text
    # res_data
    #   msg
    #   type
    def process(self, proc_data):

        # system guard
        if(self.current_user == ''):
            self.current_user = proc_data['line_uid']
        
        if(self.current_user != proc_data['line_uid']):
            return res_data
            
        if(proc_data['group'] != None):
            self.process_group(proc_data)
            
        elif (proc_data['room'] != None):
            self.process_room(proc_data)

        return proc_data

    def process_room(self, proc_data):
        pass

    # addimg [all]
    # keyword
    # <image>
    def process_group(self, proc_data):
        res_data = {'msg': '', 'type':0 }
        # default single line mode
        if(not self.interactive):
            if(addtext.match(proc_data['text'])):
                self.interactive = True
                self.proce_type = 'text'
                self.type = 1
            elif(addimg.match(proc_data['text'])):
                self.interactive = True
                self.proce_type = 'image'
                self.type = 2
            else:
                self.process_cmd(proc_data)

        # interactive mode
        if(self.interactive == True):
            self.process_interactive(proc_data)

    def operation_data(self, proc_data, group='bbl'):
        pass
    
    def process_interactive(self, process_data):
        if(self.step == 0):
            res_data['msg'] = 'input keyword'
            res_data['type'] = 1            
            self.step = 1
        elif(self.step == 1):
            self.key = proc_data['text']
            res_data['msg'] = 'input image'
            res_data['type'] = 1
            self.setp = 2
        elif(self.step == 2):
            self.value = proc_data['text']
            if(self.proce_type == image):
                # download image from line
                # upload image to imgur
                pass
            # write to data base
            if(self.group == 'bbl' or self.group == 'all'):
                self.bbl_cmd_t.cmd_id = self.key
                self.bbl_cmd_t.cmd_rsp = self.value
                self.bbl_cmd_t.cmd_type = self.type
                
                db.session.add(self.bbl_cmd_t)
                db.session.commit()

            elif(self.group == 'moe' or self.group == 'all'):
                self.moe_cmd_t.cmd_id = self.key
                self.moe_cmd_t.cmd_rsp = self.value
                self.moe_cmd_t.cmd_type = self.type

                db.session.add(self.moe_cmd_t)
                db.session.commit()                
            
            res_data['msg'] = 'finish'
            res_data['type'] = 1
            self.setp = 0
            self.current_user = ''
            self.interactive = True

    # [cmd][type][title][time][position]
    # [op][12][test][05020600]
    # [add[test][jell][1]
    # [del][test][jell][1]
    def process_cmd(self, proc_data):
        table = self.bbl_instance_t

        str_list = proc_data['text'].splite(" ")
        opcode = str_list[0]
        # open team
        if(opcode == 'op'):
            table.title = str_list[2]
            
            pass
        elif(opcode == 'add'):
            pass
        elif(opcode == 'del'):
            pass