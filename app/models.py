from app import db
from datetime import datetime, date, time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5


class IzletUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    izlet_id = db.Column(db.Integer, db.ForeignKey('izlet.id'))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    picture = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    napravljeni_izleti = db.relationship('Izlet', backref='creator', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)




class Izlet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    description = db.Column(db.String(140))
    location = db.Column(db.String(140))
    lat = db.Column(db.Numeric)
    lng = db.Column(db.Numeric)
    transport = db.Column(db.String(70))
    #timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    begin = db.Column(db.Date, index=True)
    end = db.Column(db.Date, index=True)
    picture = db.Column(db.String(200))
    cost = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return '<Izlet {}>'.format(self.name)






@login.user_loader
def load_user(id):
    return User.query.get(int(id))