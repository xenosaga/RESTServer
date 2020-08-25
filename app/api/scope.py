from ..sys_model import \
    group_t

class scope():

    def __init__(self):
        self._scopes = {}
        self._init_data = False

    # gid       type    scpoe
    # bbl12345  1       bbl
    # moe12345  1       moe

    def get_scope(self, gid):
        if(not self._init_data):
            grp = group_t()
            res = grp.get_scopes()
            for item in res:
                self._scopes[item.gid] = [item.id_type, item.scope]

            self._init_data = True
        
        try:
            scope = self._scopes[gid]
            return [scope, [1, 'shr']]
        except :
            return ['shr']