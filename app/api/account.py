from ..sys_model import account_t

class account():

    def __init__(self):
        self._account = {}
        self._init_data = False

    # line_uid  line_id   priority
    # admuid    adm       2
    # superuid  super     3
    # useruid   user      1

    def check_priority(self, cmd_info, uid):
        if(not self._init_data):
            accnt = account_t()
            res = accnt.get_accounts()
            for item in res:
                self._account[item.line_uid] = [item.line_id, item.priority]

            self._init_data = True
        
        print(self._account)
        print(cmd_info)
        print(uid)

        try:
            accnt = self._account[uid]
            if accnt[1] >= cmd_info[1]:
                return True
            return False
        except:
            return False
