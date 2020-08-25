from . import db

# line account table
class account_t(db.Model):
    __tablename__ = 'account_t'
    id = db.Column(db.Integer(), primary_key=True)
    line_uid = db.Column(db.String(256))
    line_id = db.Column(db.String(64))
    priority = db.Column(db.Integer())

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_account_by_uid(cls, uid):
        return cls.query.filter_by(line_uid=uid)

    @classmethod
    def get_admins(cls, p):
        return cls.query.filter(cls.priority >= p).all()

    @classmethod
    def get_accounts(cls):
        return cls.query.all()
        
    def __repr__(self):
        return '<Account_t %r>' % self.line_uid

# line group table
class group_t(db.Model):
    __tablename__ = "group_t"
    gid = db.Column(db.String(256), primary_key=True)
    id_type = db.Column(db.Integer())
    scope = db.Column(db.String(16))

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    @classmethod
    def get_scope_by_gid(cls, gid):
        return cls.query.filter_by(gid=gid).first()

    @classmethod
    def get_scopes(cls):
        return cls.query.all()

    def __repr__(self):
        return '<Group_t %r>' % self.scope

# line command table
class command_t(db.Model):
    __tablename__ = "command_t"
    cmd = db.Column(db.String(32), primary_key=True)
    cmd_code = db.Column(db.String(16))
    cmd_lv = db.Column(db.Integer())

    def add(self):
        db.session.add(self)
        db.session.commit(self)

    def delete(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_commands(cls):
        return cls.query.all()

    def __repr__(self):
        return '<Command_t %r>' % self.cmd_code

# line command table
class manage_t(db.Model):
    __tablename__ = "manage_t"
    id = db.Column(db.Integer(), primary_key=True)
    keyword = db.Column(db.String(256))

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_keywords(cls):
        return cls.query.all()

    def __repr__(self):
        return '<Manage_t %r>' % self.keyword

# line bot state table
class bot_state(db.Model):
    __tablename__ = 'bot_state_t'
    item_text = db.Column(db.String(64), primary_key=True)
    item_value = db.Column(db.String(64))

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    @classmethod
    def get_env(cls, text):
        return cls.query.filter_by(item_text=text)

    def __repr__(self):
        return '<Bot State_t %r>' % self.item_text