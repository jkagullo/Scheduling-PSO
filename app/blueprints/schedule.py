from flask import Blueprint, render_template, request

schedule = Blueprint('schedule', __name__)

@schedule.route('/schedule')
def schedule_page():
    return render_template('schedule.html')