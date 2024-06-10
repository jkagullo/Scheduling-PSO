from flask import Blueprint, render_template, request
from app.utils.pso_scheduler import run_pso
from time import sleep

form = Blueprint('form', __name__)

@form.route('/form')
def form_page():
    return render_template('form.html')

@form.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Parse the data
    sched_name = data['schedName']
    sections = data['sections']
    rooms = data['roomSchedule']
    professors = data['professors']

    # Change positions
    professors = {name: {'preferred_time': info['preferred_time'], 'preferred_subjects': info['preferred_subjects']} for name, info in professors.items()}
    
    # PSO Algorithm for scheduling
    run_pso(sched_name, sections, rooms, professors)
    
    return 'Success!'



