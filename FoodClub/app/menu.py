from flask import url_for
def menu():
    menu = {
        'Home': url_for('main.home'),
        'New recipe': url_for('main.newRecipe'),
        'Profile': url_for('main.profile'),
        'Sign In': url_for('auth.signin'),
        'Sign Up': url_for('auth.signup')
    }
    return menu