from . import db
from datetime import datetime

class Permission:
    QUERY = 0x01
    QUEST = 0x02
    EDITOR = 0x04
    DELETE = 0x08
    ADMINISTER = 0x10

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permission = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')
    
    def __repr__(self):
        return '<Role %r>' % self.name

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.QUERY |
                     Permission.QUEST, True),
            'Moderator': (Permission.QUERY | 
                          Permission.EDITOR |
                          Permission.DELETE, False),
            'Administrator': (0xff, False)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)

        db.session.commit()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    line_id = db.Column(db.Unicode(64), unique=True, index=True)
    line_uid = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    process_lock = db.Column(db.Boolean, default=False)
    last_word = db.Column(db.Unicode(128))

    # 傳入 command 的 permissions
    def can(self, permissions):
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __repr__(self):
        return '<User %r>' % self.line_id

class History(db.Model):
    __tablename__ = 'history_log'
    id = db.Column(db.Integer, primary_key=True)
    line_uid = db.Column(db.String(256), db.ForeignKey('users.line_uid'))
    line_msg = db.Column(db.Unicode(512))
    line_group = db.Column(db.String(256))
    timestame = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<History %r>' % self.line_msg

class Guild(db.Model):
    __tablename__ = 'guild'
    id = db.Column(db.Integer, primary_key=True)
    guild_name = db.Column(db.Unicode(30))
    line_id = db.Column(db.String(64))
    line_uid = db.Column(db.String(256))
    game_id = db.Column(db.String(16))

    def __repr__(self):
        return '<Guild %r>' % self.guild_name

class Instence(db.Model):
    __tablename__ = 'instance'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode(256))
    game_type = db.Column(db.String(16))
    date_time = db.Column(db.DateTime)
    max_player = db.Column(db.Integer)
    cur_palyer = db.Column(db.Integer, default=1)
    users = db.relationship('Gplayer', backref='instance', lazy='dynamic')

    def __repr__(self):
        return '<Instance %r>' % self.title


class Gplayer(db.Model):
    __tablename__ = 'gplayer'
    id = db.Column(db.Integer, primary_key=True)
    inst_title = db.Column(db.Unicode(256), db.ForeignKey('instance.title'))
    game_id = db.Column(db.Unicode(16))
    line_uid = db.Column(db.String(256))
    team_id = db.Column(db.Integer)

    def __repr__(self):
        return '<GPlayer %r>' % self.game_id


class Command(db.Model):
    __tablename__ = 'command'
    id = db.Column(db.Integer, primary_key=True)
    cmd_word = db.Column(db.Unicode(128), unique=True, index=True)
    cmd_code = db.Column(db.String(30), unique=True)
    premission = db.Column(db.Integer)

    def __repr__(self):
        return '<Command %r>' % self.cmd_code

class Gdata(db.Model):
    __tablename__ = 'gdata'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.Unicode(128), unique=True, index=True)
    response = db.Column(db.Unicode(128))
    rtype = db.Column(db.Integer)

    def __repr__(self):
        return '<Gdata %r>' % self.keyword