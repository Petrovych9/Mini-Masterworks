from flask import Blueprint,render_template

mainBlueprint = Blueprint('main', __name__)
adminBlueprint = Blueprint('admin', __name__)

#main
@mainBlueprint.route("/")
def index():
    return "Hello fucking world"





#admin