import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None
    SECRET_KEY = None

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'   
    SQLITE_DB_DIR = os.path.join(basedir, "../instance")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "db.sqlite3")  
    SECRET_KEY = "shhh.... its very secret"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    SECURITY_TRACKABLE = True
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'admin@a.com'

    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 0
    CACHE_DEFAULT_TIMEOUT = 60

    DEBUG = True

