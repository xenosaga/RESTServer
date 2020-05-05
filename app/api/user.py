import datetime
from .. import db
from ..chat_models \
    import cmd_t, history_t, guild_t, \
        instance_t, instance_player_t
from flask import jsonify


# state less object
class user:

    def __init__(self, model_type):
        self.line_id = ''
        self.query = ''
        self.res_data = {'msg':'', 'type':0}
        self.type = model_type
        self.time_formate = '%Y%m%d-%H%M'
    
    # proc_data
    #   room_id <option>
    #   group_id <option>
    #   line_uid
    #   text
    #   type
    def process(self, proc_data, scope):
        if(proc_data.get('room_id') != None):
            self.processRoom(proc_data, scope)
        elif(proc_data.get('group_id') != None):
            self.processGroup(proc_data, scope)
            print('process')

        return self.res_data

    def processRoom(self, proc_data, scope):
        
        pass

    # res_data
    #   res
    #   type
    def processGroup(self, proc_data, scope):
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
                print('---------guild-----------')
                self.process_guild(proc_data, scope)
            # keyword
            else:
                print('---------keyword---------')
                self.process_query(proc_data, scope)
        # instance
        else:
            self.process_cmd(str_list, proc_data['line_uid'])
            pass

    # [op_in][12][test][05020600]            
    def instance_open(self, str_list, line_uid):
        inst_table = instance_t(self.type)
        
        inst_table.game_type = str_list[1]
        inst_table.title = str_list[2]
        dto = datetime.datetime.strptime(str_list[3], self.time_formate)
        inst_table.date_time = dto
        inst_table.scope = self.type
        res = inst_table.get_game_by_title(str_list[2], self.type)
        
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

    # [del_in][title]
    def instance_delete(self, str_list, line_uid):
        inst_table = instance_t(self.type)

        inst_table.title = str_list[1]
        inst_table.scope = self.type

        print(str_list[1], self.type)
        res = inst_table.get_game_by_title(str_list[1], self.type)
        print('-----------------------------')
        print(res)
        if(res == None):
            self.res_data['msg'] = 'No such instance'
            self.res_data['type'] = 1
            return
        
        res.delete()
        self.res_data['msg'] = str_list[1] + ' is deleted'
        self.res_data['type'] = 1

    # [add_p][test][jell][1]
    def instance_add_player(self, str_list, line_uid):
        inst_table = instance_t(self.type)
        inst_user_table = instance_player_t(self.type)
        inst_res = inst_table.get_game_by_title(title=str_list[1], scope=self.type)
        
        if(inst_res == None):
            self.res_data['msg'] = 'No game'
            self.res_data['type'] = 1
            return
        else:
            inst_user_table.title = inst_res.title
            inst_user_table.game_id = str_list[2]
            inst_user_table.game_type = inst_res.game_type
            inst_user_table.line_uid = line_uid
            inst_user_table.scope = self.type
            team_id = int(str_list[3])
            
            # Invalid id error
            if(team_id <= 0 or team_id > inst_res.max_player):
                self.res_data['msg'] = 'invalid team id'
                self.res_data['type'] = 1
                return 
            
            inst_user_table.team_id = team_id
            inst_user_res = inst_user_table.get_player(title=inst_res.title,\
                 id=team_id, scope=self.type)
        
            # Same team id error
            if(inst_user_res != None):
                self.res_data['msg'] = 'same team id'
                self.res_data['type'] = 1
                return
            
            # add to db
            inst_user_table.add()
            self.res_data['msg'] = 'Add team success'
            self.res_data['type'] = 1
            
    # [del][test][1]
    def instance_delete_player(self, str_list, line_uid):
        inst_user_table = instance_player_t(self.type)

        inst_user_table.title = str_list[1]
        inst_user_table.team_id = str_list[2]
        inst_user_res = inst_user_table.get_player(title=str_list[1], \
            id=str_list[2], scope=self.type)

        if(inst_user_res != None):
            if(inst_user_res.line_uid != line_uid):
                self.res_data['msg'] = 'This is not you'
                self.res_data['type'] = 1
            else:
                inst_user_res.delete()
                self.res_data['msg'] = 'delete success'
                self.res_data['type'] = 1
        else:
            self.res_data['msg'] = 'No such user'
            self.res_data['type'] = 1

    # [q_inst][title]
    def instance_query(self, str_list):
        # list all instance
        if(str_list[1] == 'all'):
            inst_t = instance_t(self.type)
            inst_res = inst_t.get_games(scope=self.type)
            
            for item in inst_res:
                print(item.title + '\t' + str(item.max_player) + '\t' + str(item.date_time))
            self.res_data['msg'] = 'all data'
            self.res_data['type'] = 1

        # list member by title
        else:
            inst_user_t = instance_player_t(self.type)
            inst_user_res = inst_user_t.get_players_by_title(title=str_list[1], \
                scope=self.type)

            if(inst_user_res == None):
                self.res_data['msg'] = 'No such game'
                self.res_data['type'] = 1
            
            for item in inst_user_res:
                print(str(item.team_id) + ' ' + item.game_id + ' ' + item.title)
            self.res_data['msg'] = 'list success'
            self.res_data['type'] = 1

    # [cmd][type][title][time][position]
    def process_cmd(self, str_list, line_uid):

        opcode = str_list[0]
        # open team
        # [op_in][12][test][05020600]
        if(opcode == 'op_in'):
            self.instance_open(str_list, line_uid)
        # [del_in][title]
        elif(opcode == 'del_in'):
            self.instance_delete(str_list, line_uid)
        # [add_p][test][jell][1]
        elif(opcode == 'add_p'):
            self.instance_add_player(str_list, line_uid)
        # [del_p][test][jell][1]
        elif(opcode == 'del_p'):
            self.instance_delete_player(str_list, line_uid)
        # [q_inst][title]
        elif(opcode == 'q_inst'):
            self.instance_query(str_list)

    def process_query(self, proc_data, scope):
        scope_l = ['shr', scope]
        cmd_table = cmd_t('')
        res = cmd_table.get_cmd(cmd_key=proc_data['text'],
                                scope=scope_l)
        # has data
        if(res != None):
            self.res_data['msg'] = res.cmd_rsp
            self.res_data['type'] = res.cmd_type

    def process_guild(self, proc_data, scope):
        res_text = ''
        db_val = bbl_guild_t.query.first()
        print(type(db_val))
        # for l_id, l_uid, g_id in :
        #     res_text = res_text + l_id + ' : ' + g_id + '\n'
        self.res_data['msg'] = res_text
        self.res_data['type'] = 1

        pass