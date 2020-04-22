
from .. import db
from ..moe_models import moe_cmd_t, moe_history_t, moe_guild_t, moe_instance_t
from ..bbl_models import bbl_cmd_t, bbl_history_t, bbl_guild_t, bbl_instance_t


# state less object
class user:

    def __init__(self, type):
        self.line_id = ''
        self.query = ''
        self.res = ''
        self.type = type
        if(self.type == 'bbl'):
            self.cmd_t = bbl_guild_t()
            self.history_t = bbl_history_t()
            self.guild_t = bbl_guild_t()
            self.instance_t = bbl_instance_t()
        elif(self.type == 'moe')
            self.cmd_t = moe_guild_t()
            self.history_t = moe_history_t()
            self.guild_t = moe_guild_t()
            self.instance_t = moe_instance_t()
    
    # proc_data
    #   key
    #   value
    def process(self, proc_data):
        if(proc_data['room_id'] not None):
            self.processRoom(proc_data)
        elif(proc_data['group_id'] not None):
            self.processGroup(proc_data)

    def processRoom(self, proc_data):
        
        pass

    # res_data
    #   res
    #   type
    def processGroup(self, proc_data):
        res_data = {}
        res_data['type'] = 0
        res_data['res'] = ''
        
        if(proc_data['key'] == 'guild'):
            res_data['res'] = self._guild_t.query.all()
        elif(proc_data['key'] == 'instance'):
            res_data['res'] = self.instance_t.query.all()
        else
            self.cmd_t.cmd_id = proce_data['key']
            res_data['res'] = self.cmd_t.query.all()
        
        return res_data


