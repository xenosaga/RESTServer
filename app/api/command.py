from ..sys_model import command_t

class command():

    def __init__(self):
        self._commend = {}
        self._init_data = False
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
            i = 0
            for item in res:
                self._commend[item.cmd] = [item.cmd_code, item.cmd_lv]

            self._init_data = True
        
        try :
            cmd = self._commend[text]
            return cmd
        except :
            cmd = ['', 0]
            return cmd
                