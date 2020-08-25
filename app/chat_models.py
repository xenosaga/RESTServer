from . import db
from sqlalchemy import or_
from sqlalchemy import asc

class keyword_t(db.Model):
    __tablename__ = 'cmd_t'
    keyword_id = db.Column(db.Integer, primary_key=True)
    keyword_key = db.Column(db.Unicode(128))
    keyword_rsp = db.Column(db.Unicode(128))
    keyword_type = db.Column(db.Integer)
    keyword_scope = db.Column(db.String(32))

    def __init__(self, name):
        self.name = name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_cmd(cls, keyword_key, scope):
        return cls.query.filter(cls.keyword_key == keyword_key, 
                                cls.keyword_scope.in_(scope)).first()

    @classmethod
    def get_cmds_by_key(cls, keyword_key):
        return cls.query.filter(cls.keyword_key == keyword_key).all()
    
    @classmethod
    def get_all_cmd(cls, scope):
        return cls.query.filter(cls.keyword_scope.in_(scope)).all()

    def __repr__(self):
        return '<Cmd_t %r>' %  self.keyword_key
      
class history_t(db.Model):
    __tablename__ = 'history_t'
    id = db.Column(db.Integer, primary_key=True)
    line_uid = db.Column(db.String(256))
    line_msg = db.Column(db.Unicode(512))
    line_group = db.Column(db.String(256))
    scope = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime)
    
    def __init__(self, name):
        self.name = name

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_msgs_by_uid(cls, line_uid, scope):
        return cls.query.filter(cls.line_uid == line_uid, 
                                cls.scope.in_(scope)).all()

    @classmethod
    def get_msgs_by_scope(cls, scope):
        return cls.query.filter_by(scope = scope).all()

    @classmethod
    def get_all_message(cls):
        return cls.query.all()

    def __repr__(self):
        return '< %s History_t %r>' % self.name, self.line_msg

class guild_t(db.Model):
    __tablename__ = 'guild_t'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.String(64))
    line_uid = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    scope = db.Column(db.String(32))

    def __init__(self, name):
        self.name = name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def query_by_line(cls, line_id, scope):
        return cls.query.filter(cls.line_id == line_id,
                                cls.scope.in_(scope)).all()

    @classmethod
    def query_by_game_id(cls, game_id, scope):
        return cls.query.filter(cls.game_id == game_id,
                                cls.scope.in_(scope)).all()

    @classmethod
    def get_all(cls, scope):
        return cls.query.filter(cls.scope.in_(scope)).all()

    def __repr__(self):
        return '<Guild_t %r>' % self.line_id

class instance_t(db.Model):
    __tablename__ = 'instance_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_type = db.Column(db.String(16))
    date_time = db.Column(db.DateTime)
    max_player = db.Column(db.Integer)
    scope = db.Column(db.String(32))

    def __init__(self, name):
        self.name = name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_game_by_title(cls, title, scope):
        return cls.query.filter_by(title=title, scope=scope).first()

    @classmethod
    def get_games(cls, scope):
        return cls.query.filter_by(scope=scope).all()

    def __repr__(self):
        return '<Instance_t %r>' % self.title

class instance_player_t(db.Model):
    __tablename__ = 'instance_player_t'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    game_id = db.Column(db.String(16))
    game_type = db.Column(db.String(16))
    line_uid = db.Column(db.String(256))
    team_id = db.Column(db.Integer())
    scope = db.Column(db.String(32))

    def __init__(self, name):
        self.name = name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_player(cls, title, id, scope):
        return cls.query.filter_by(title=title, team_id=id, scope=scope).first()

    @classmethod
    def get_players_by_title(cls, title, scope):
        return cls.query.filter(cls.title == title, 
            cls.scope == scope).order_by(asc(cls.team_id))

    def __repr__(self):
        return '<Instance_player_t %r>' % self.title

