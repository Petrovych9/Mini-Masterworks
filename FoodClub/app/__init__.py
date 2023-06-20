from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"]='ajnjfgfhfn!1tyuiop[92vgb9r5'

    # Register blueprints or import modules
    from .views import mainBlueprint,adminBlueprint, authBlueprint
    app.register_blueprint(mainBlueprint)
    app.register_blueprint(adminBlueprint, url_prefix='/admin')
    app.register_blueprint(authBlueprint, url_prefix='/authentication')


    return app
