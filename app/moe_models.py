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

    def __repr__(self):
        return '<MOE Cmd_t %r>' % self.name
      
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

    def update(self):
        db.session.commit()

    def __repr__(self):
        return '<MOE History_t %r>' % self.name

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

    def __repr__(self):
        return '<MOE Guild_t %r>' % self.name

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

    def __repr__(self):
        return '<MOE Instance_t %r>' % self.name

