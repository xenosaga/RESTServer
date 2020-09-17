from ..sys_model import command_t

class cmd():

    def __init__(self):
        self._commend = {}
        self._init_data = False

    def get_cmd_code(self, text):
        param_list = text.split(" ")
        cmd_t = command_t()
        row = cmd_t.query_command(param_list[0])
        
        # default 查詢命令
        cmd_code = 0
        cmd_privilege = 0
        is_valid = True
        
        # 在命令列表李
        if( row != None):
            cmd_code = row.cmd_code
            cmd_privilege = row.cmd_lv
        else :
            # 非查詢列表
            if (len(param_list) > 1 ):
                is_valid = False
        
        return [cmd_code, cmd_privilege, is_valid]

    # cmd           code
    # query         0
    # addimg        1
    # addtext       2
    # guild         10
    # inst_op       11
    # inst_del      12
    # inst_add_p    13
    # inst_del_p    14
    # inst_query    15
    def check_command(self, text):
        if(not self._init_data):
            cmd = command_t()
            res = cmd.get_commands()
            for item in res:
                self._commend[item.cmd] = [item.cmd_code, item.cmd_lv]

            self._init_data = True
 
        try :
            cmd = self._commend[text]
            return cmd
        except :
            cmd = ['0', 1]
            return cmd
                