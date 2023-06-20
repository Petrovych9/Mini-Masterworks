from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"]='ajnjfgfhfn!1tyuiop[92vgb9r5'

    # Register blueprints or import modules
    import views
    app.register_blueprint(views.mainBlueprint)
    app.register_blueprint(views.adminBlueprint, url_prefix='/admin')
    app.register_blueprint(views.authBlueprint, url_prefix='/authentication')


    return app
