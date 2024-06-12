from flask import Blueprint, render_template, request
import json
import os

schedule = Blueprint('schedule', __name__)


def remove_duplicate_keys(subjects):
    unique_keys = set()
    unique_subjects = {}

    for key, value in subjects.items():
        if key not in unique_keys:
            unique_keys.add(key)
            unique_subjects[key] = value

    return unique_subjects


@schedule.route('/schedule')
def schedule_page():
    # Time slot duration basis
    time_slots = {
        'D1_H1': {'day': 'Monday', 'start': 7, 'end': 8},
        'D1_H2': {'day': 'Monday', 'start': 8, 'end': 9},  # 8:00 AM to 9:00 AM
        'D1_H3': {'day': 'Monday', 'start': 9, 'end': 10},  # 9:00 AM to 10:00 AM
        'D1_H4': {'day': 'Monday', 'start': 10, 'end': 11},  # 10:00 AM to 11:00 AM
        'D1_H5': {'day': 'Monday', 'start': 11, 'end': 12},  # 11:00 AM to 12:00 PM
        'D1_H6': {'day': 'Monday', 'start': 12, 'end': 13},  # 12:00 PM to 1:00 PM
        'D1_H7': {'day': 'Monday', 'start': 13, 'end': 14},  # 1:00 PM to 2:00 PM
        'D1_H8': {'day': 'Monday', 'start': 14, 'end': 15},  # 2:00 PM to 3:00 PM
        'D1_H9': {'day': 'Monday', 'start': 15, 'end': 16},  # 3:00 PM to 4:00 PM
        'D1_H10': {'day': 'Monday', 'start': 16, 'end': 17},  # 4:00 PM to 5:00 PM
        'D1_H11': {'day': 'Monday', 'start': 17, 'end': 18},  # 5:00 PM to 6:00 PM
        'D1_H12': {'day': 'Monday', 'start': 18, 'end': 19},
        'D1_H13': {'day': 'Monday', 'start': 19, 'end': 20},

        'D2_H1': {'day': 'Tuesday', 'start': 7, 'end': 8},
        'D2_H2': {'day': 'Tuesday', 'start': 8, 'end': 9},  # 8:00 AM to 9:00 AM
        'D2_H3': {'day': 'Tuesday', 'start': 9, 'end': 10},  # 9:00 AM to 10:00 AM
        'D2_4': {'day': 'Tuesday', 'start': 10, 'end': 11},  # 10:00 AM to 11:00 AM
        'D2_H5': {'day': 'Tuesday', 'start': 11, 'end': 12},  # 11:00 AM to 12:00 PM
        'D2_H6': {'day': 'Tuesday', 'start': 12, 'end': 13},  # 12:00 PM to 1:00 PM
        'D2_H7': {'day': 'Tuesday', 'start': 13, 'end': 14},  # 1:00 PM to 2:00 PM
        'D2_H8': {'day': 'Tuesday', 'start': 14, 'end': 15},  # 2:00 PM to 3:00 PM
        'D2_H9': {'day': 'Tuesday', 'start': 15, 'end': 16},  # 3:00 PM to 4:00 PM
        'D2_H10': {'day': 'Tuesday', 'start': 16, 'end': 17},  # 4:00 PM to 5:00 PM
        'D2_H11': {'day': 'Tuesday', 'start': 17, 'end': 18},  # 5:00 PM to 6:00 PM
        'D2_H12': {'day': 'Tuesday', 'start': 18, 'end': 19},
        'D2_H13': {'day': 'Tuesday', 'start': 19, 'end': 20},

        'D3_H1': {'day': 'Wednesday', 'start': 7, 'end': 8},
        'D3_H2': {'day': 'Wednesday', 'start': 8, 'end': 9},  # 8:00 AM to 9:00 AM
        'D3_H3': {'day': 'Wednesday', 'start': 9, 'end': 10},  # 9:00 AM to 10:00 AM
        'D3_4': {'day': 'Wednesday', 'start': 10, 'end': 11},  # 10:00 AM to 11:00 AM
        'D3_H5': {'day': 'Wednesday', 'start': 11, 'end': 12},  # 11:00 AM to 12:00 PM
        'D3_H6': {'day': 'Wednesday', 'start': 12, 'end': 13},  # 12:00 PM to 1:00 PM
        'D3_H7': {'day': 'Wednesday', 'start': 13, 'end': 14},  # 1:00 PM to 2:00 PM
        'D3_H8': {'day': 'Wednesday', 'start': 14, 'end': 15},  # 2:00 PM to 3:00 PM
        'D3_H9': {'day': 'Wednesday', 'start': 15, 'end': 16},  # 3:00 PM to 4:00 PM
        'D3_H10': {'day': 'Wednesday', 'start': 16, 'end': 17},  # 4:00 PM to 5:00 PM
        'D3_H11': {'day': 'Wednesday', 'start': 17, 'end': 18},  # 5:00 PM to 6:00 PM
        'D3_H12': {'day': 'Wednesday', 'start': 18, 'end': 19},
        'D3_H13': {'day': 'Wednesday', 'start': 19, 'end': 20},

        'D4_H1': {'day': 'Thursday', 'start': 7, 'end': 8},
        'D4_H2': {'day': 'Thursday', 'start': 8, 'end': 9},  # 8:00 AM to 9:00 AM
        'D4_H3': {'day': 'Thursday', 'start': 9, 'end': 10},  # 9:00 AM to 10:00 AM
        'D4_4': {'day': 'Thursday', 'start': 10, 'end': 11},  # 10:00 AM to 11:00 AM
        'D4_H5': {'day': 'Thursday', 'start': 11, 'end': 12},  # 11:00 AM to 12:00 PM
        'D4_H6': {'day': 'Thursday', 'start': 12, 'end': 13},  # 12:00 PM to 1:00 PM
        'D4_H7': {'day': 'Thursday', 'start': 13, 'end': 14},  # 1:00 PM to 2:00 PM
        'D4_H8': {'day': 'Thursday', 'start': 14, 'end': 15},  # 2:00 PM to 3:00 PM
        'D4_H9': {'day': 'Thursday', 'start': 15, 'end': 16},  # 3:00 PM to 4:00 PM
        'D4_H10': {'day': 'Thursday', 'start': 16, 'end': 17},  # 4:00 PM to 5:00 PM
        'D4_H11': {'day': 'Thursday', 'start': 17, 'end': 18},  # 5:00 PM to 6:00 PM
        'D4_H12': {'day': 'Thursday', 'start': 18, 'end': 19},
        'D4_H13': {'day': 'Thursday', 'start': 19, 'end': 20},

        'D5_H1': {'day': 'Friday', 'start': 7, 'end': 8},
        'D5_H2': {'day': 'Friday', 'start': 8, 'end': 9},  # 8:00 AM to 9:00 AM
        'D5_H3': {'day': 'Friday', 'start': 9, 'end': 10},  # 9:00 AM to 10:00 AM
        'D5_H4': {'day': 'Friday', 'start': 10, 'end': 11},  # 10:00 AM to 11:00 AM
        'D5_H5': {'day': 'Friday', 'start': 11, 'end': 12},  # 11:00 AM to 12:00 PM
        'D5_H6': {'day': 'Friday', 'start': 12, 'end': 13},  # 12:00 PM to 1:00 PM
        'D5_H7': {'day': 'Friday', 'start': 13, 'end': 14},  # 1:00 PM to 2:00 PM
        'D5_H8': {'day': 'Friday', 'start': 14, 'end': 15},  # 2:00 PM to 3:00 PM
        'D5_H9': {'day': 'Friday', 'start': 15, 'end': 16},  # 3:00 PM to 4:00 PM
        'D5_H10': {'day': 'Friday', 'start': 16, 'end': 17},  # 4:00 PM to 5:00 PM
        'D5_H11': {'day': 'Friday', 'start': 17, 'end': 18},  # 5:00 PM to 6:00 PM
        'D5_H12': {'day': 'Friday', 'start': 18, 'end': 19},
        'D5_H13': {'day': 'Friday', 'start': 19, 'end': 20}
    }

    # TUP COS UNITS BASIS
    subjects = {
        "CC141L-M": {
            "type": "lab",
            "units": 1
        },
        "CC142-M": {
            "type": "lec",
            "units": 2
        },
        "CC103-M": {
            "type": "lec",
            "units": 3
        },
        "CS123-M": {
            "type": "lec",
            "units": 3
        },
        "GEC2-M": {
            "type": "lec",
            "units": 3
        },
        "GEC3-M": {
            "type": "lec",
            "units": 3
        },
        "GEC5-M": {
            "type": "lec",
            "units": 3
        },
        "MATHA35-M": {
            "type": "lec",
            "units": 5
        },
        "NSTP2-M": {
            "type": "lec",
            "units": 3
        },
        "PE2-M": {
            "type": "lec",
            "units": 2
        },
        "CC201L-M": {
            "type": "lab",
            "units": 1
        },
        "CC202-M": {
            "type": "lec",
            "units": 2
        },
        "CC223-M": {
            "type": "lec",
            "units": 3
        },
        "CS201L-M": {
            "type": "lab",
            "units": 1
        },
        "CS202--M": {
            "type": "lec",
            "units": 2
        },
        "CS221L--M": {
            "type": "lab",
            "units": 1
        },
        "CS222--M": {
            "type": "lec",
            "units": 2
        },
        "CS243-M": {
            "type": "lec",
            "units": 3
        },
        "CS261L-M": {
            "type": "lab",
            "units": 1
        },
        "CS262-M": {
            "type": "lec",
            "units": 2
        },
        "PE3-M": {
            "type": "lec",
            "units": 3
        },
        "CC303-M": {
            "type": "lec",
            "units": 3
        },
        "CS303-M": {
            "type": "lec",
            "units": 3
        },
        "CS321L-M": {
            "type": "lab",
            "units": 1
        },
        "CS322-M": {
            "type": "lec",
            "units": 2
        },
        "CS343-M": {
            "type": "lec",
            "units": 3
        },
        "CS361L-M": {
            "type": "lab",
            "units": 1
        },
        "CS362-M": {
            "type": "lec",
            "units": 2
        },
        "CSE3-M": {
            "type": "lec",
            "units": 3
        },
        "CSE4-M": {
            "type": "lec",
            "units": 3
        },
        "CS403": {
            "type": "lab",
            "units": 6
        },
        "CS423": {
            "type": "lec",
            "units": 3
        },
        "IT123-M": {
            "type": "lec",
            "units": 3
        },
        "MATHSTAT03-M": {
            "type": "lec",
            "units": 3
        },
        "NSTP2--M": {
            "type": "lec",
            "units": 3
        },
        "IT201L--M": {
            "type": "lec",
            "units": 1
        },
        "IT202--M": {
            "type": "lec",
            "units": 2
        },
        "IT223-M": {
            "type": "lec",
            "units": 3
        },
        "IT241L-M": {
            "type": "lab",
            "units": 1
        },
        "IT242-M": {
            "type": "lec",
            "units": 2
        },
        "IT261L-M": {
            "type": "lec",
            "units": 1
        },
        "IT262-M": {
            "type": "lec",
            "units": 2
        },
        "ITE1-M": {
            "type": "lec",
            "units": 3
        },
        "PE4-M": {
            "type": "lec",
            "units": 2
        },
        "GEE11D-M": {
            "type": "lec",
            "units": 3
        },
        "IT303--M": {
            "type": "lec",
            "units": 3
        },
        "IT323": {
            "type": "lec",
            "units": 3
        },
        "IT343_M": {
            "type": "lec",
            "units": 3
        },
        "IT363-M": {
            "type": "lec",
            "units": 3
        },
        "ITE4-M": {
            "type": "lec",
            "units": 3
        },
        "IT406-M": {
            "type": "lab",
            "units": 9
        },
        "IT423--M": {
            "type": "lec",
            "units": 3
        },
        "IS123-M": {
            "type": "lec",
            "units": 3
        },
        "IS203-M": {
            "type": "lec",
            "units": 3
        },
        "IS223-M": {
            "type": "lec",
            "units": 3
        },
        "IS243-M": {
            "type": "lec",
            "units": 3
        },
        "IS263-M": {
            "type": "lec",
            "units": 3
        },
        "ISE1-M": {
            "type": "lec",
            "units": 3
        },
        "IS303-M": {
            "type": "lec",
            "units": 3
        },
        "IS323-M": {
            "type": "lec",
            "units": 3
        },
        "IS343-M": {
            "type": "lec",
            "units": 3
        },
        "IS363-M": {
            "type": "lec",
            "units": 3
        },
        "IS383-M": {
            "type": "lec",
            "units": 3
        },
        "ISE4-M": {
            "type": "lec",
            "units": 3
        },
        "IS406-M": {
            "type": "lab",
            "units": 9
        },
        "IS423-M": {
            "type": "lec",
            "units": 3
        }
    }
    data = None     

    try:
        # Check if the created schedules file exists
        if os.path.exists('app/static/schedule.json'):
            
            # Load the json schedules
            with open('app/static/schedule.json', 'r') as f:
                data = json.load(f)

            # Parse the section key text
            data = {key.replace("Section ", ""): value for key, value in data.items()}

            # Sort in ascending by professor name
            for section, info in data.items():
                data[section] = sorted(info, key=lambda x: x[2])

            # Get the expected duration of time based on given format and its respected type and units
            for section, info in data.items():
                for i in range(len(info)):
                    sub_code = data[section][i][1]

                    if sub_code in subjects:
                        sched_time_format = data[section][i][3]
                        sched_time_dict = time_slots[sched_time_format]
                        if (subjects[sub_code]['type'] == 'lec'):
                            # multiply units by 1 
                            unit_multiplier = 1
                        elif (subjects[sub_code]['type'] == 'lab'):
                            # multiply units by 3 
                            unit_multiplier = 3
                        data[section][i][3] = f"{sched_time_dict['day'][:3] + ' ' + str(sched_time_dict['start']) + ':00 - ' + str(sched_time_dict['start'] + subjects[sub_code]['units'] * unit_multiplier) + ':00'}"
        else:
            print("Error: The file 'schedule.json' does not exist.")
            data = None

    except Exception as e:
        print("An error occurred:", str(e))
        data = None


    return render_template('schedule.html', data=data)