import os

class Config:
    
   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
   
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgres://heesvoedbpsfod:2016c6fb2c9ccd1886cd0f4a0712e889a1ad0c0914d8e0f93c21e735978ebc21@ec2-52-86-56-90.compute-1.amazonaws.com:5432/dapbi750074o22"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://norah:1234we@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}