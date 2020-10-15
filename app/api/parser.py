from ..models import Role, User, Command
from .utilty import AddText, AddImg, AddSticker, \
        ModImg, ModSticker, ModText, \
        Query, DeleteImg, Delete, GuildList, \
        InstOpen, InstDelete, InstQuery, \
        InstAddPlayer, InstDelPlayer, \
        PostbackInst
from .emu import CommandCode

class parser():

    def __init__(self):
        self._commend = {}
        self._init_data = False


    def parse_text(self, text):
        param_list = text.split(" ")
        row = Command.query.filter_by(cmd_word=param_list[0]).first()
        print(row)
        # default 查詢命令
        cmd_code = 0
        premission = 0
        
        # 在命令列表李(非查命令)
        if( row != None):
            cmd_code = row.cmd_code
            premission = row.premission
        
        return [cmd_code, param_list, premission]

    def check_command(self, text):
        if(not self._init_data):
            cmd = Command()
            res = cmd.query.all()
            for item in res:
                self._commend[item.cmd] = [item.cmd_code, item.permission]

            self._init_data = True
 
        try :
            cmd = self._commend[text]
            return cmd
        except :
            cmd = ['0', 1]
            return cmd
                
    def process_keyword(self, cmd_code, param, line_uid, msg_id, sid, pid):
        print('process keyword')
        print('cmd_code : ', cmd_code)
        print('Command code: ', CommandCode.MOD_IMG)

        if( cmd_code == CommandCode.QUERY ):
            return Query(param)
        elif( cmd_code == CommandCode.ADD_IMG):
            return AddImg(line_uid, param)
        elif( cmd_code == CommandCode.ADD_TEXT):
            return AddText(line_uid, param)
        elif( cmd_code == CommandCode.ADD_STICKER):
            return AddSticker(line_uid, param)
        elif( cmd_code == CommandCode.MOD_IMG ):
            return ModImg(line_uid, msg_id)
        elif( cmd_code == CommandCode.MOD_TEXT ):
            return ModText(line_uid, param)
        elif( cmd_code == CommandCode.MOD_STICKER ):
            return ModSticker(line_uid, sid, pid)
        elif( cmd_code == CommandCode.DELETE_IMG ):
            return DeleteImg(param)
        elif( cmd_code == CommandCode.DELETE):
            return Delete(param) 
        elif( cmd_code == CommandCode.GUILD):
            return GuildList()
        elif( cmd_code == CommandCode.INST_OPEN):
            return InstOpen(line_uid, param)
        elif( cmd_code == CommandCode.INST_DELETE):
            return InstDelete(line_uid, param)
        elif( cmd_code == CommandCode.INST_ADD_PLAYER):
            return InstAddPlayer(line_uid, param)
        elif( cmd_code == CommandCode.INST_DELETE_PLAYER):
            return InstDelPlayer(line_uid, param)
        elif( cmd_code == CommandCode.INST_QUERY):
            return InstQuery()
        pass

    def process_pb(self, data, param):
        PostbackInst(data, param['datetime'])

        pass