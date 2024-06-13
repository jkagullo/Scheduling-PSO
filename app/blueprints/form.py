from flask import Blueprint, render_template, request
from app.utils.pso_scheduler import run_pso
from app.utils.pso_scheduler2 import run_pso2
from time import sleep
import os

form = Blueprint('form', __name__)

@form.route('/form')
def form_page():
    return render_template('form.html')

@form.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    counter = 0

    # Parse the data
    sched_name = data['schedName']
    sections = data['sections']
    rooms = data['roomSchedule']
    professors = data['professors']
    semester = data['semester']

    # Change positions
    professors = {name: {'preferred_time': info['preferred_time'], 'preferred_subjects': info['preferred_subjects']} for name, info in professors.items()}

    if semester == '1st':
        run_pso(sched_name, sections, rooms, professors)
    elif semester == '2nd':
        run_pso2(sched_name, sections, rooms, professors)
    else:
        print("Invalid semester: ", semester)
    return 'Success!'



