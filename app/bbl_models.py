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
    game_type = db.Column(db.String(16))
    date_time = db.Column(db.DateTime)
    max_player = db.Column(db.Integer

    def __repr__(self):
        return '<BBL Instance_t %r>' % self.name

class bbl_instance_player_t(db.Model):
    __tablename__ = 'bbl_instance_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    game_type = db.Column(db.String(16))
    line_uid = db.Column(db.String(256))
    team_id = db.Column(db.Integer())

    def __repr__(self):
        return '<BBL Instance_t %r>' % self.name

