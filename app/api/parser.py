from ..models import Role, User, Command
from .utilty import AddText, AddImg, AddSticker, \
        ModImg, ModSticker, ModText, \
        Query, DeleteImg, Delete

class CommandCode:
    QUERY = 0
    ADD_IMG = 1
    ADD_TEXT = 2
    ADD_STICKER = 3
    MOD_IMG = 4
    MOD_TEXT = 5
    MOD_STICKER = 6
    DELETE_IMG = 7
    DELETE = 8
    GUILD = 10
    INST_OPEN = 11
    INST_DELETE = 12
    INST_ADD_PLAYER = 13
    INST_DELETE_PLAYER = 14

class parser():

    def __init__(self):
        self._commend = {}
        self._init_data = False


    def parse_text(self, text):
        param_list = text.split(" ")
        cmd = Command()
        row = cmd.query.filter_by(cmd_word=param_list[0]).first()
        
        # default 查詢命令
        cmd_code = 0
        permission = 0
        
        # 在命令列表李(非查命令)
        if( row != None):
            cmd_code = row.cmd_code
            permission = row.permission
        
        return [cmd_code, param_list, permission]

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
                
    def process_keyword(self, cmd_code, param, line_uid):
        if( cmd_code == CommandCode.QUERY ):
            return Query(param)
        elif( cmd_code == CommandCode.ADD_IMG):
            return AddImg(line_uid, param)
        elif( cmd_code == CommandCode.ADD_TEXT):
            return AddText(line_uid, param)
        elif( cmd_code == CommandCode.ADD_STICKER):
            return AddSticker(line_uid, param)
        elif( cmd_code == CommandCode.MOD_IMG ):
            return ModImg(line_uid, param)
        elif( cmd_code == CommandCode.MOD_TEXT ):
            return ModText(line_uid, param)
        elif( cmd_code == CommandCode.MOD_STICKER ):
            return ModSticker(line_uid, param)
        elif( cmd_code == CommandCode.DELETE_IMG ):
            return DeleteImg(param)
        elif( cmd_code == CommandCode.DELETE):
            return Delete(param) 
        pass