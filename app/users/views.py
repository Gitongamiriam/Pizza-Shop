from flask import render_template, Blueprint
from forms import 

users = Blueprint("users", __name__)

@users.route('/register',methods=['GET', 'POST'])
def register():
    form=FlaskForm
    return render_template('register.html' form = form)