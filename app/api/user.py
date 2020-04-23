import datetime
from .. import db
from ..moe_models import moe_cmd_t, moe_history_t, moe_guild_t, moe_instance_t
from ..bbl_models import bbl_cmd_t, bbl_history_t, bbl_guild_t, bbl_instance_t


# state less object
class user:

    def __init__(self, type):
        self.line_id = ''
        self.query = ''
        self.res_data = {'msg':'', 'type':0}
        self.type = type
        self.time_formate = '%y%m%d-%H%M'
        if(self.type == 'bbl'):
            self.cmd_t = bbl_guild_t()
            self.history_t = bbl_history_t()
            self.guild_t = bbl_guild_t()
            self.instance_t = bbl_instance_t()
            self.instance_player_t = bbl_instance_player_t()
        elif(self.type == 'moe')
            self.cmd_t = moe_guild_t()
            self.history_t = moe_history_t()
            self.guild_t = moe_guild_t()
            self.instance_t = moe_instance_t()
            self.instance_player_t = moe_instance_player_t
    
    # proc_data
    #   room_id <option>
    #   group_id <option>
    #   text
    #   type
    def process(self, proc_data):
        if(proc_data['room_id'] not None):
            self.processRoom(proc_data)
        elif(proc_data['group_id'] not None):
            self.processGroup(proc_data)

        return self.res_data

    def processRoom(self, proc_data):
        
        pass

    # res_data
    #   res
    #   type
    def processGroup(self, proc_data):
        self.res_data['msg'] = ''
        self.res_data['type'] = 0

        str_list = proc_data['text']
        
        # guild, query
        if(len(str_list) == 1):
            # guild
            if(str_list[0] == 'guild'):
                self.res_data['msg'] = self._guild_t.query.all()
                self.res_data['type'] = 1
            # keyword
            else:
                self.cmd_t.cmd_id = str_list[0]
                res = self.cmd_t.query.first()
                self.res_data['msg'] = res['cmd_rsp']
                self.res_data['type'] = res['cmd_type']
        # instance
        else:
            self.process_cmd(str_list)
            


    # [cmd][type][title][time][position]
    # [op][12][test][05020600]
    # [add[test][jell][1]
    # [del][test][jell][1]
    def process_cmd(self, str_list, line_uid):
        inst_table = self.instance_t
        inst_user_table = self.instance_player_t

        str_list = proc_data['text'].splite(" ")
        opcode = str_list[0]
        # open team
        if(opcode == 'op'):
            inst_table.game_type = str_list[1]
            inst_table.title = str_list[2]
            dto = datetime.datetime.striptime(str_list[3], self.time_formate)
            inst_table.date_time = dto
            res = inst_table.query.filter_by(title=str_list[1]).first()
            if(res != None):
                self.res_data['msg'] = 'Insert error'
                self.res_data['type'] = 1
            else:
                inst_table.max_player = 6
                if(str_list[1] == '12'):
                    inst_table.max_player = 12
                db.session.add(inst_table)
                db.session.commit() 
                self.res_data['msg'] = 'Create success'
                self.res_data['type'] = 1
        elif(opcode == 'add'):
            res = inst_table.filter_by(title=str_list[1]).first()
            if(res):
                inst_user_table.title = res['title']
                inst_user_table.game_id = str_list[2]
                inst_user_table.game_type = res['game_type']
                inst_user_table.line_uid = line_uid
                team_id = int(str_list[3])
                
                # Invalid id error
                if(team_id <= 0 or team_id > res['max_player']):
                    self.res_data['msg'] = 'invalid team id'
                    self.res_data['type'] = 1
                    return 

                inst_user_table.team_id = team_id
                res = inst_user_table.query.filter_by(title=res['title'], team_id=team_id)
                # Same team id error
                if(res not None):
                    self.res_data['msg'] = 'same team id'
                    self.res_data['type'] = 1
                    return
                
                db.session.add(inst_user_table)
                db.session.commit()
            else:
                self.res_data['msg'] = 'No game'
                self.res_data['type'] = 1

        elif(opcode == 'del'):

            inst_user_table.title
            pass

    def process_query(self, proc_data):
        pass