from flask import Blueprint, render_template, request

schedname = Blueprint('schedname', __name__)

@schedname.route('/schedname')
def schedname_page():
    return render_template('schedname.html')