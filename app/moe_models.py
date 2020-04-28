from . import db

class moe_cmd_t(db.Model):
    __tablename__ = 'moe_cmd_t'
    cmd_id = db.Column(db.Unicode(128), primary_key=True)
    cmd_rsp = db.Column(db.Unicode(128))
    cmd_type = db.Column(db.Integer)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_cmd(cls, cmd_id):
        return cls.query.filter_by(cmd_id=cmd_id).first()

    @classmethod
    def get_all_cmd(cls, cmd_id):
        return cls.query.filter_by(cmd_id=cmd_id).all()

    def __repr__(self):
        return '<MOE Cmd_t %r>' % self.cmd_id
      
class moe_history_t(db.Model):
    __tablename__ = 'moe_history_t'
    id = db.Column(db.Integer, primary_key=True)
    line_uid = db.Column(db.String(256))
    line_msg = db.Column(db.Unicode(512))
    timestamp = db.Column(db.DateTime)
    
    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_msgs_by_uid(cls, line_uid):
        return cls.query.filter_by(line_uid=line_uid).all()

    @classmethod
    def get_all_message(cls):
        return cls.query.all()

    def __repr__(self):
        return '<MOE History_t %r>' % self.line_msg

class moe_guild_t(db.Model):
    __tablename__ = 'moe_guild_t'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(64))
    line_uid = db.Column(db.String(256))
    game_id = db.Column(db.String(16))

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def query_by_line(cls, line_id):
        return cls.query.filter_by(line_id=line_id).all()

    @classmethod
    def query_by_game_id(cls, game_id):
        return cls.query.filter_by(game_id=game_id).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def __repr__(self):
        return '<MOE Guild_t %r>' % self.line_id

class moe_instance_t(db.Model):
    __tablename__ = 'moe_instance_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_type = db.Column(db.String(16))
    line_uid = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    team_id = db.Column(db.Integer())

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_game_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def __repr__(self):
        return '<MOE Instance_t %r>' % self.title


class moe_instance_player_t(db.Model):
    __tablename__ = 'moe_instance_player_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    game_type = db.Column(db.String(16))
    line_uid = db.Column(db.String(256))
    team_id = db.Column(db.Integer())

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_player(cls, title, id):
        return cls.query.filter_by(title=title, team_id=id).all()

    def __repr__(self):
        return '<MOE Instance_player_t %r>' % self.title