import couchdb
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()

couch = couchdb.Server(Config.COUCHDB_SERVER)
logger_db = couch[Config.COUCHDB_DATABASE]

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.products.routes import products
    from flaskblog.orders.routes import orders
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    from flaskblog.logs.routes import logs
    from flaskblog.notifications.routes import notifications
    app.register_blueprint(users)
    app.register_blueprint(products)
    app.register_blueprint(orders)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(logs)
    app.register_blueprint(notifications)

    return app
