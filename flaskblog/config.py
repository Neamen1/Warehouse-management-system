import os
from datetime import timedelta
import redis

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    COUCHDB_SERVER = os.environ.get('COUCHDB_SERVER')
    COUCHDB_DATABASE = os.environ.get('COUCHDB_DATABASE')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # Flask-Session
    SESSION_TYPE = os.environ.get('SESSION_TYPE')
    SESSION_REDIS = redis.from_url(os.environ.get('SESSION_REDIS'))
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)  # Set the session timeout to 30 minutes

    # FLASK_APP="flaskblog.py"
    # FLASK_ENV="development"
    # SQLALCHEMY_DATABASE_URI="sqlite:///storage.db"
    # SECRET_KEY="5791628bb0b13ce0c676dfde280ba245"
    # COUCHDB_SERVER="http://couchdb:couchdb@localhost:5984/"
    # COUCHDB_DATABASE="logs"