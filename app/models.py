from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,id,title,content,category,likes,dislikes):
        self.id =id
        self.title = title
        self.content = content
        self.category = category 
        self.likes = likes 
        self.dislikes = dislikes

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    pass_secure = db.Column(db.String(255))



    def __repr__(self):
        return f'User {self.username}'


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'