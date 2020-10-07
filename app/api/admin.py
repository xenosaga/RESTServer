
# from .. import db
# from ..chat_models import \
#     keyword_t, history_t, guild_t, instance_t
# import re

# # state less object
# class admin:

#     def __init__(self):
#         self._current_user = ''        
#         self._next_type = None

#         self.key = ''
#         self.value = ''
#         self.scope = ['bbl']
#         self.type = 1
#         self.init = False
#         self.res_data = {'msg': 'no premission',
#                          'type': 0
#                         }

#     # check if in edit mode
#     def edit_mode(self):
#         return self._is_edit

#     # check admin
#     def check_admin(self, uid):
#         return (self._current_user == uid)

#     # proce_data
#     #   line_uid
#     #   text
#     # res_data
#     #   msg
#     #   type
#     def process_key(self, proc_data, cmd_code, scope):

#         # print('curr user: ' + self._current_user)
#         # print(proc_data['line_uid'])

#         if(self._current_user == ''):
#             self._current_user = proc_data['line_uid']
            
#             # image type
#             if cmd_code[0] == '1':
#                 self._next_type = 1
#                 self.res_data['msg'] = 'input image'
            
#             # text type
#             else:
#                 self._next_type = 0
#                 self.res_data['msg'] = 'input text'
#             self.res_data['type'] = 1

#         sc = scope[0]
#         # group mode
#         if(sc[0] == 1):
#             self.process_group(proc_data, scope)
        
#         # room mode 
#         elif (sc[0] == 0):
#             self.process_room(proc_data, scope)

#         return self.res_data

#     def process_data(self, proc_data, cmd_code, scope):
#         # image type
#         if self._next_type == 1:
#             pass
#         # text type
#         else:
#             self.process_group_data
#             pass

#     def process_room(self, proc_data):
#         pass

#     # addimg [all]
#     # keyword
#     # <image>
#     def process_group_key(self, proc_data, scope):
#         # default single line mode
#         str_list = proc_data['text'].split(" ")
        
#         print(str_list)
#         # mod scope ( for initial )
#         if len(str_list) == 3:
#             self._key = str_list[1]
#             if scope[0][1] != 'shr':
#                 self._scope = scope

#         elif len(str_list) == 2:
#             self._key = str_list[1]
#             self._scope = [scope[0][0]]

#     def process_group_data(self, proc_data):
#         # command and keyword
#         if(str_list[0] == 'addimg'):
#             self.proce_type = 'image'
#             self.type = 2
#             self.key = str_list[1]
#         elif(str_list[0] == 'addtext'):
#             self.proce_type = 'text'
#             self.type = 1
#             self.key = str_list[1]
#         # value save data
#         else:
#             print('save value')
#             if(self.type == 1):
#                 self.write_text(proc_data['text'])
#             elif(self.type == 2):
#                 self.write_image(proc_data['text'])
                
#     def write_db(self):
#         print('---------- write db -----------')
#         print(self.scope)

#         cmd_table = cmd_t(self.scope[0])
#         cmd_table.cmd_key = self.key
#         cmd_table.cmd_rsp = self.value
#         cmd_table.cmd_scope = self.scope[0]
#         cmd_table.cmd_type = self.type

#         # share command
#         if(len(self.scope) > 1):
#             cmd_table.cmd_scope = 'shr'
#             res = cmd_table.get_cmds_by_key(cmd_key=self.key)
#         else:
#             res = cmd_table.get_cmd(cmd_key=self.key, scope=self.scope)
        
#         print(res)
        
#         # delete others 
#         if(res != [] or res != None):
#             for item in res :
#                 item.delete()
#         # add record
#         cmd_table.add()

#     def write_image(self, value):
#         # download image from line
#         # upload image to imgur
#         self.value = "url to imgur"
#         self.write_db()
#         self.res_data['msg'] = 'img saved'
#         self.res_data['type'] = 1

#     def write_text(self, value):
#         self.value = value
#         self.write_db()
#         self.res_data['msg'] = 'text saved'
#         self.res_data['type'] = 1

#     def clear_state(self):
#         self.current_user = ''
#         self.init = False