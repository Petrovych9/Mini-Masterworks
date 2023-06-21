from flask import Blueprint,render_template, request, url_for
from .menu import menu

mainBlueprint = Blueprint('main', __name__)


#main
@mainBlueprint.route("/", methods=["GET", ' POST'])
def home():
    return render_template('base.html', menu=menu())


@mainBlueprint.route('/new-recipe')
def newRecipe():
    pass


@mainBlueprint.route('/profile')
def profile():
    pass