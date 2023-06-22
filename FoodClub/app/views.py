from flask import Blueprint,render_template, request, url_for
from flask_login import current_user, login_required
from .menu import menu

mainBlueprint = Blueprint('main', __name__)


#main
@mainBlueprint.route("/", methods=["GET", ' POST'])
@login_required
def home():
    return render_template('base.html', menu=menu(), user=current_user)


@mainBlueprint.route('/new-recipe')
@login_required
def newRecipe():
    pass


@mainBlueprint.route('/profile')
@login_required
def profile():
    pass