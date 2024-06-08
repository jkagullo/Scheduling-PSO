from flask import Blueprint, render_template, request

form = Blueprint('form', __name__)

@form.route('/form')
def form_page():
    return render_template('form.html')