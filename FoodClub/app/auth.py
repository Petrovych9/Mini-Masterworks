import flask
from flask import Blueprint, render_template, request ,url_for
from .views import menu

authBlueprint = Blueprint('auth', __name__)


@authBlueprint.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        firstName = request.form['firstname']
        lastName = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        print(firstName, lastName, email, phone, password)

        if firstName == "":
            flask.flash('Enter the First name', category="error")
        elif lastName == "":
            flask.flash('Enter the Last name', category="error")
        elif email == "@gmail.com":
            flask.flash('Enter the Email', category="error")
        elif len(phone) < 3:
            flask.flash('Invalid phone number', category="error")
        elif len(password) < 1:
            flask.flash('Password too short', category="error")
        else: flask.flash('Account created', category="success")

    return render_template('signUP.html', menu=menu(), email='@gmail.com', phone='+380')


@authBlueprint.route("/sign-in", methods=["GET", 'POST'])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        print(email,password)

        if email == "@gmail.com":
            flask.flash('Enter the Email', category="error")
        elif len(password) < 1:
            flask.flash('Password too short', category="error")
        else:
            flask.redirect(url_for('main.home'))
            flask.flash('Welcome', category="success")

    return render_template('signIN.html', menu=menu(), email='@gmail.com')
