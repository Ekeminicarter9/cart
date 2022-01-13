from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
views = Blueprint('views', __name__) 

@views.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Test</h1>"
@login_requireddef home(): 
 return render_template("home.html", user=current_user)
