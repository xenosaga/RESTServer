from . import db

class bbl_cmd_t(db.Model):
    __tablename__ = 'bbl_cmd_t'
    cmd_id = db.Column(db.Unicode(128), primary_key=True)
    cmd_rsp = db.Column(db.Unicode(128))
    cmd_type = db.Column(db.Integer)

    def __repr__(self):
        return '<BBL Cmd_t %r>' % self.name
      
class bbl_history_t(db.Model):
    __tablename__ = 'bbl_history_t'
    id = db.Column(db.Integer, primary_key=True)
    line_uid = db.Column(db.String(256))
    line_msg = db.Column(db.Unicode(512))
    timestamp = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<BBL History_t %r>' % self.name

class bbl_guild_t(db.Model):
    __tablename__ = 'bbl_guild_t'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(64))
    line_uid = db.Column(db.String(256))
    game_id = db.Column(db.String(16))

    def __repr__(self):
        return '<BBL Guild_t %r>' % self.name

class bbl_instance_t(db.Model):
    __tablename__ = 'bbl_instance_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    team_id = db.Column(db.Integer())

    def __repr__(self):
        return '<BBL Instance_t %r>' % self.name

class moe_cmd_t(db.Model):
    __tablename__ = 'moe_cmd_t'
    cmd_id = db.Column(db.Unicode(128), primary_key=True)
    cmd_rsp = db.Column(db.Unicode(128))
    cmd_type = db.Column(db.Integer)

    def __repr__(self):
        return '<MOE Cmd_t %r>' % self.name
      
class moe_history_t(db.Model):
    __tablename__ = 'moe_history_t'
    id = db.Column(db.Integer, primary_key=True)
    line_uid = db.Column(db.String(256))
    line_msg = db.Column(db.Unicode(512))
    timestamp = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<MOE History_t %r>' % self.name

class moe_guild_t(db.Model):
    __tablename__ = 'moe_guild_t'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(64))
    line_uid = db.Column(db.String(256))
    game_id = db.Column(db.String(16))

    def __repr__(self):
        return '<MOE Guild_t %r>' % self.name

class moe_instance_t(db.Model):
    __tablename__ = 'moe_instance_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    team_id = db.Column(db.Integer())

    def __repr__(self):
        return '<MOE Instance_t %r>' % self.name

class account_t(db.Model):
    __tablename__ = 'account_t'
    id = db.Column(db.Integer(), primary_key=True)
    line_uid = db.Column(db.String(256))
    pority = db.Column(db.Integer())

    def __repr__(self):
        return '<Account_t %r' % self.name

class bot_state(db.Model):
    __tablename__ = 'bot_state_t'
    item_text = db.Column(db.String(64), primary_key=True)
    item_value = db.Column(db.String(64))

    def __repr__(self):
        return '<Bot State_t %r>' % self.name