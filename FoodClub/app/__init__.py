from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'ajnjfgfhfn!1tyuiop[92vgb9r5'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    # Register blueprints
    from .views import mainBlueprint
    from .admin import adminBlueprint
    from .auth import authBlueprint

    app.register_blueprint(mainBlueprint, url_prefix='/')
    app.register_blueprint(adminBlueprint, url_prefix='/admin/')
    app.register_blueprint(authBlueprint, url_prefix='/auth/')

    from .models import User, Recipe

    create_database(app)

    return app


def create_database(app):
    if not os.path.exists('./' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Database created!")
