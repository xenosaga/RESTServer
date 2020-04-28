import datetime
from .. import db
from ..moe_models import moe_cmd_t, moe_history_t, moe_guild_t, moe_instance_t
from ..bbl_models import bbl_cmd_t, bbl_history_t, bbl_guild_t, bbl_instance_t, bbl_instance_player_t
from flask import jsonify

# state less object
class user:

    def __init__(self, type):
        self.line_id = ''
        self.query = ''
        self.res_data = {'msg':'', 'type':0}
        self.type = type
        self.time_formate = '%Y%m%d-%H%M'
        if(self.type == 'bbl'):
            self.cmd_t = bbl_guild_t
            self.history_t = bbl_history_t()
            self.guild_t = bbl_guild_t()
            self.instance_t = bbl_instance_t()
            self.instance_player_t = bbl_instance_player_t()
        elif(self.type == 'moe'):
            self.cmd_t = moe_guild_t()
            self.history_t = moe_history_t()
            self.guild_t = moe_guild_t()
            self.instance_t = moe_instance_t()
            self.instance_player_t = moe_instance_player_t
    
    # proc_data
    #   room_id <option>
    #   group_id <option>
    #   line_uid
    #   text
    #   type
    def process(self, proc_data):
        if(proc_data.get('room_id') != None):
            self.processRoom(proc_data)
        elif(proc_data.get('group_id') != None):
            self.processGroup(proc_data)
            print('process')

        return self.res_data

    def processRoom(self, proc_data):
        
        pass

    # res_data
    #   res
    #   type
    def processGroup(self, proc_data):
        # default response                
        self.res_data['msg'] = ''
        self.res_data['type'] = 0

        str_list = proc_data['text'].split(" ")
        print("len: " + str(len(str_list)))

        # guild, query
        if(len(str_list) == 1):
            print('query')
            # guild
            if(str_list[0] == 'guild'):
                res_text = ''
                db_val = bbl_guild_t.query.first()
                print(type(db_val))
                # for l_id, l_uid, g_id in :
                #     res_text = res_text + l_id + ' : ' + g_id + '\n'
                self.res_data['msg'] = res_text
                self.res_data['type'] = 1
            # keyword
            else:
                self.cmd_t.cmd_id = str_list[0]
                res = self.cmd_t.query.first()

                if(res != None):
                    self.res_data['msg'] = res['cmd_rsp']
                    self.res_data['type'] = res['cmd_type']
        # instance
        else:
            self.process_cmd(str_list, proc_data['line_uid'])
            pass

    # [op][12][test][05020600]            
    def instance_open(self, str_list, line_uid):
        inst_table = self.instance_t
        
        inst_table.game_type = str_list[1]
        inst_table.title = str_list[2]
        dto = datetime.datetime.strptime(str_list[3], self.time_formate)
        inst_table.date_time = dto
        res = inst_table.get_game_by_title(str_list[2])
        
        if(res != None):
            self.res_data['msg'] = 'Insert error'
            self.res_data['type'] = 1
        else:
            inst_table.max_player = 6
            if(str_list[1] == '12'):
                inst_table.max_player = 12
            inst_table.add()
            self.res_data['msg'] = 'Create success'
            self.res_data['type'] = 1
    
    # [add[test][jell][1]
    def instance_add(self, str_list, line_uid):
        inst_table = self.instance_t
        inst_user_table = self.instance_player_t
        res = inst_table.get_game_by_title(title=str_list[1])
        
        if(res != None):
            inst_user_table.title = res.title
            inst_user_table.game_id = str_list[2]
            inst_user_table.game_type = res.game_type
            inst_user_table.line_uid = line_uid
            team_id = int(str_list[3])
            
            # Invalid id error
            if(team_id <= 0 or team_id > res.max_player):
                self.res_data['msg'] = 'invalid team id'
                self.res_data['type'] = 1
                return 
            
            inst_user_table.team_id = team_id
            res = inst_user_table.get_player(title=res.title, id=team_id)
        
            # Same team id error
            if(res != None):
                self.res_data['msg'] = 'same team id'
                self.res_data['type'] = 1
                return
            
            # add to db
            inst_user_table.add()
            self.res_data['msg'] = 'Add team success'
            self.res_data['type'] = 1
            
        else:
            self.res_data['msg'] = 'No game'
            self.res_data['type'] = 1

    # [del][test][1]
    def instance_delete(self, str_list, line_uid):
        inst_user_table = self.instance_player_t

        inst_user_table.title = str_list[1]
        inst_user_table.team_id = str_list[2]
        res = inst_user_table.get_player(title=str_list[1], id=str_list[2])
        if(res != None):
            if(res.line_uid != line_uid):
                self.res_data['msg'] = 'This is not you'
                self.res_data['type'] = 1
            else:
                res.delete()
                self.res_data['msg'] = 'delete success'
                self.res_data['type'] = 1
        else:
            self.res_data['msg'] = 'No such user'
            self.res_data['type'] = 1


    # [cmd][type][title][time][position]
    def process_cmd(self, str_list, line_uid):
        inst_table = self.instance_t
        inst_user_table = self.instance_player_t

        opcode = str_list[0]
        # open team
        # [op][12][test][05020600]
        if(opcode == 'op'):
            self.instance_open(str_list, line_uid)
        # [add[test][jell][1]
        elif(opcode == 'add'):
            self.instance_add(str_list, line_uid)
        # [del][test][jell][1]
        elif(opcode == 'del'):
            self.instance_delete(str_list, line_uid)


    def process_query(self, proc_data):
        pass