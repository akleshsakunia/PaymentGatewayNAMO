import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "randomuuid"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class TestConfig(Config):
    TESTING = True


