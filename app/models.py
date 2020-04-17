from . import db

class cmd_t(db.Model):
    __tablename__ = 'cmd_t'
    cmd_id = db.Column(db.Unicode(128), primary_key=True)
    cmd_rsp = db.Column(db.Unicode(128))
    cmd_type = db.Column(db.Integer)

    def __repr__(self):
        return '<Cmd_t %r>' % self.name
      
class history_t(db.Model):
    __tablename__ = 'history_t'
    id = db.Column(db.Integer, primary_key=True)
    line_uid = db.Column(db.String(256))
    line_msg = db.Column(db.Unicode(512))
    timestamp = db.Column(db.DateTime)
    
    def __repr__(self):
        return '<History_t %r>' % self.name
