from ..sys_model import \
    group_t

class scope():

    def __init__(self):
        self._scopes = {}
        self._init_data = False

    def query_group_name(self, gid):
        if(not self._init_data):
            grp = group_t()
            res = grp.get_scopes()
            for item in res:
                self._scopes[item.gid] = [item.id_type, item.gname]

            self._init_data = True
        

        try:
            return self._scopes[gid]
        except :
            print("no scope")
            return [0, 'none']