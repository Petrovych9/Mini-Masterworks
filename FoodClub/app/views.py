from flask import Blueprint,render_template

mainBlueprint = Blueprint('main', __name__)
adminBlueprint = Blueprint('admin', __name__)
authBlueprint = Blueprint('authentication', __name__)

menu = ['Home', 'New recipe', 'Profile', '1111' ]


#main
@mainBlueprint.route("/")
def index():
    return render_template('base.html', menu=menu)


#admin