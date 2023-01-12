# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
# migrate = Migrate()

bootstrap = Bootstrap()  # instance of class bootstrap
login_manager = LoginManager() # instance of class LoginManager
login_manager.login_view = 'authentaction.do_the_login'
login_manager.session_protection='strong'

bcrypt = Bcrypt()# instance of class Bcrypt


def create_app(config_type):
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)
    db.init_app(app)
    # migrate.init_app(app, db)
    bootstrap.init_app(app)  # initialize bootstrap
    login_manager.init_app(app) # initialize login manager
    bcrypt.init_app(app) # initialize bcrypt 

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)


    return app
