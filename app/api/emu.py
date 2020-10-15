class UserLockType:
    UNLOCK          = 0
    TEXT_LOCK       = 1
    IMG_LOCK        = 2
    STICKER_LOCK    = 3
    INST_LOCK       = 4
   
class RspDataType:
    SILENT  = 0
    TEXT    = 1
    IMG     = 2
    STICKER = 3
    FLEX    = 4

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
    INST_QUERY = 13
    INST_ADD_PLAYER = 14
    INST_DELETE_PLAYER = 15