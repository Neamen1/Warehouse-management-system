import os


class Config:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SECRET_KEY = 'secret_key_for_testing'
    WTF_CSRF_ENABLED = False

    COUCHDB_SERVER = 'http://couchdb:couchdb@localhost:5984/'
    COUCHDB_DATABASE = 'logs'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    FLASK_APP = "flaskblog.py"
    FLASK_ENV = "development"

