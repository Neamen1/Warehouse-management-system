set FLASK_APP=flaskblog.py
set FLASK_ENV=development
set SQLALCHEMY_DATABASE_URI=sqlite:///storage.db
set SECRET_KEY=5791628bb0b13ce0c676fde280a245
set COUCHDB_SERVER=http://couchdb:couchdb@localhost:5984/
set COUCHDB_DATABASE=logs
set SESSION_TYPE=redis
set SESSION_REDIS=redis://localhost:6379/
pytest
pause