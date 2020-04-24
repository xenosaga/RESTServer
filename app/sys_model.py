from . import db

class account_t(db.Model):
    __tablename__ = 'account_t'
    id = db.Column(db.Integer(), primary_key=True)
    line_uid = db.Column(db.String(256))
    pority = db.Column(db.Integer())

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return '<Account_t %r' % self.name

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
        
    def __repr__(self):
        return '<Bot State_t %r>' % self.name