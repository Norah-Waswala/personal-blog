from sqlalchemy import ForeignKey
from . import db,login_manager
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    username = db.Column(db.String(225),unique = True,nullable = False)
    email  = db.Column(db.String(225),unique = True,nullable = False)
    secure_password = db.Column(db.String(225),nullable = False)
    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
   

    @property
    def set_password(self):
        raise AttributeError('You cannot read the password attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User {self.username}'

       
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(255))
    # email = db.Column(db.String(255), unique=True, index=True)
    # password_secure = db.Column(db.String(255))
    # description = db.Column(db.String(255))
    # avatar = db.Column(db.String())
    # blogs = db.relationship('Blog', backref='author', lazy = 'dynamic')

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    blog = db.Column(db.Text(), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    comment = db.relationship('Comment',backref='blog',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.Column(db.String(255), index = True,nullable = False)
    
    
    def save_b(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()   
    def get_blog(id):
        blog = Blog.query.filter_by(id=id).first()
    
    def __repr__(self):
        return f'Blog {self.blog}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    
    @classmethod
    def get_comments(cls,blog_id):
        comments = Comment.query.filter_by(blog_id=blog_id).all()

        return comments
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.remove(self)
        db.session.commit()

    def __repr__(self):
        return f'comment:{self.comment}'

class Subscriber(db.Model):
    __tablename__='subscribers'

    id=db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True,index=True)

    def save_subscriber(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Subscriber {self.email}'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
