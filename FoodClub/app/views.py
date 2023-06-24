import flask
from flask import Blueprint,render_template, request, url_for
from flask_login import current_user, login_required
from .menu import menu
from .models import Recipe
from . import db

mainBlueprint = Blueprint('main', __name__)


#main
@mainBlueprint.route("/", methods=["GET", ' POST'])
@login_required
def home():
    return render_template('base.html', menu=menu(), user=current_user)

def check_image(image):
    img = image.read()
    if img == b'':
        def_image_path = 'D:\BOHDAN PETROVYCH\progr\MyMainProjects\FoodClub/app\static\images/new_recipe\default.jpg'
        with open(def_image_path, 'rb') as def_image:
            def_img = def_image.read()
        return def_img
    else:
        return img

@mainBlueprint.route('/new-recipe', methods=["POST", 'GET'])
@login_required
def new_recipe():
    if request.method == "POST":
        dish_name = request.form['dish_name']
        cooking_time = request.form['cooking_time']
        description = request.form['description']
        ingredients = request.form['ingredients']
        image = request.files['photo']
        image = check_image(image)
        new_rec = Recipe(
            dish_name=dish_name,
            cooking_time=cooking_time,
            description=description,
            ingredients=ingredients,
            image=image,
            user_id=current_user.id)
        db.session.add(new_rec)
        db.session.commit()
        flask.flash("Recipe created", category="success")
    return render_template('new-recipe.html', menu=menu(), user=current_user)


@mainBlueprint.route('/profile')
@login_required
def profile():
    pass