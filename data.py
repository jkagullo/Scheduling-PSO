# INPUT SECTIONS FOR (CS/IS/IT)
sections_cs = {
    1: ['Section 1A-CS', 'Section 1B-CS'],
    2: ['Section 2A-CS', 'Section 2B-CS'],
    3: ['Section 3A-CS'],
    4: ['Section 4A-CS']
}

sections_it = {
    1: ['Section 1A-IT', 'Section 1B-IT'],
    2: ['Section 2A-IT', 'Section 2B-IT'],
    3: ['Section 3A-IT'],
    4: ['Section 4A-IT']
}

sections_is = {
    1: ['Section 1A-IS', 'Section 1B-IS'],
    2: ['Section 2A-IS', 'Section 2B-IS'],
    3: ['Section 3A-IS'],
    4: ['Section 4A-IS']
}


# INPUT PROFESSORS
professors = {
    'Prof A': {'preferred_time': 'AM', 'preferred_subjects': ['CC113-M', 'CC131L-M']},
    'Prof B': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof C': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof D': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof E': {'preferred_time': '', 'preferred_subjects': ['CS233-M', 'CS333-M']},
    'Prof F': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof G': {'preferred_time': '', 'preferred_subjects': ['CS433-M', '']},
    'Prof H': {'preferred_time': '', 'preferred_subjects': ['CS413-M', 'CS272-M']},
    'Prof I': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof J': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof K': {'preferred_time': '', 'preferred_subjects': ['', '']},
    'Prof L': {'preferred_time': '', 'preferred_subjects': ['', '']},
    # Add more professors as needed
}


# PRE DEFINED SUBJECTS
subjects_CS_2 = {
    1: {'CC141L-M': {'type': 'lab', 'units': 1}, 'CC142-M': {'type': 'lec', 'units': 2}, 'CC103-M': {'type': 'lec', 'units': 3}, 'CS123-M': {'type': 'lec', 'units': 3}, 'GEC2-M': {'type': 'lec', 'units': 3}, 'GEC3-M': {'type': 'lec', 'units': 3}, 'GEC5-M': {'type': 'lec', 'units': 3}, 'MATHA35-M': {'type': 'lec', 'units': 5}, 'NSTP2-M': {'type': 'lec', 'units': 3}, 'PE2-M': {'type': 'lec', 'units': 2}},
    2: {'CC201L-M': {'type': 'lab', 'units': 1}, 'CC202-M': {'type': 'lec', 'units': 2}, 'CC223-M': {'type': 'lec', 'units': 3}, 'CS201L-M': {'type': 'lab', 'units': 1}, 'CS202--M': {'type': 'lec', 'units': 2}, 'CS221L--M': {'type': 'lab', 'units': 1}, 'CS222--M': {'type': 'lec', 'units': 2}, 'CS243-M': {'type': 'lec', 'units': 3}, 'CS261L-M': {'type': 'lab', 'units': 1}, 'CS262-M': {'type': 'lec', 'units': 2}, 'PE3-M': {'type': 'lec', 'units': 3 }},
    3: {'CC303-M': {'type': 'lec', 'units': 3}, 'CS303-M': {'type': 'lec', 'units': 3}, 'CS321L-M': {'type': 'lab', 'units': 1}, 'CS322-M': {'type': 'lec', 'units': 2}, 'CS343-M': {'type': 'lec', 'units': 3}, 'CS361L-M': {'type': 'lab', 'units': 1}, 'CS362-M': {'type': 'lec', 'units': 2}, 'CSE3-M': {'type': 'lec', 'units': 3}, 'CSE4-M': {'type': 'lec', 'units': 3}},
    4: {'CS403': {'type': 'lab', 'units': 6}, 'CS423': {'type': 'lec', 'units': 3}}
}

subjects_IT_2 = {
    1: {'CC103-M': {'type': 'lec', 'units': 3}, 'CC141L-M': {'type': 'lab', 'units': 1}, 'CC142-M': {'type': 'lec', 'units': 2}, 'GEC2-M': {'type': 'lec', 'units': 3}, 'GEC3-M': {'type': 'lec', 'units': 3}, 'GEC5-M': {'type': 'lec', 'units': 3}, 'IT123-M': {'type': 'lec', 'units': 3}, 'MATHSTAT03-M': {'type': 'lec', 'units': 3}, 'NSTP2--M': {'type': 'lec', 'units': 3}, 'PE2-M': {'type': 'lec', 'units': 2}},
    2: {'CC201L-M': {'type': 'lab', 'units': 1}, 'CC202-M': {'type': 'lec', 'units': 2}, 'CC223-M': {'type': 'lec', 'units': 3}, 'IT201L--M': {'type': 'lec', 'units': 1}, 'IT202--M': {'type': 'lec', 'units': 2}, 'IT223-M': {'type': 'lec', 'units': 3}, 'IT241L-M': {'type': 'lab', 'units': 1}, 'IT242-M': {'type': 'lec', 'units': 2}, 'IT261L-M': {'type': 'lec', 'units': 1}, 'IT262-M': {'type': 'lec', 'units': 2}, 'ITE1-M': {'type': 'lec', 'units': 3}, 'PE4-M': {'type': 'lec', 'units': 2}},
    3: {'CC303-M': {'type': 'lec', 'units': 3}, 'GEE11D-M': {'type': 'lec', 'units': 3}, 'IT303--M': {'type': 'lec', 'units': 3}, 'IT323': {'type': 'lec', 'units': 3}, 'IT343_M': {'type': 'lec', 'units': 3}, 'IT363-M': {'type': 'lec', 'units': 3}, 'ITE4-M': {'type': 'lec', 'units': 3}},
    4: {'IT406-M': {'type': 'lab', 'units': 9}, 'IT423--M': {'type': 'lec', 'units': 3}}
}

subjects_IS_2 = {
    1: {'CC103-M': {'type': 'lec', 'units': 3}, 'CC141L-M': {'type': 'lab', 'units': 1}, 'CC142-M': {'type': 'lec', 'units': 2}, 'GEC2-M': {'type': 'lec', 'units': 3}, 'GEC3-M': {'type': 'lec', 'units': 3}, 'GEC5-M': {'type': 'lec', 'units': 3}, 'IS123-M': {'type': 'lec', 'units': 3}, 'MATHSTAT03-M': {'type': 'lec', 'units': 3}, 'NSTP2--M': {'type': 'lec', 'units': 3}, 'PE2-M': {'type': 'lec', 'units': 2}},
    2: {'CC201L-M': {'type': 'lab', 'units': 1}, 'CC202-M': {'type': 'lec', 'units': 2}, 'CC223-M': {'type': 'lec', 'units': 3}, 'IS203-M': {'type': 'lec', 'units': 3}, 'IS223-M': {'type': 'lec', 'units': 3}, 'IS243-M': {'type': 'lec', 'units': 3}, 'IS263-M': {'type': 'lec', 'units': 3}, 'ISE1-M': {'type': 'lec', 'units': 3}, 'PE4-M': {'type': 'lec', 'units': 2}},
    3: {'CC303-M': {'type': 'lec', 'units': 3}, 'IS303-M': {'type': 'lec', 'units': 3}, 'IS323-M': {'type': 'lec', 'units': 3}, 'IS343-M': {'type': 'lec', 'units': 3}, 'IS363-M': {'type': 'lec', 'units': 3}, 'IS383-M': {'type': 'lec', 'units': 3}, 'ISE4-M': {'type': 'lec', 'units': 3}},
    4: {'IS406-M': {'type': 'lab', 'units': 9}, 'IS423-M': {'type': 'lec', 'units': 3}}
}


# STRUCTURE THE VARIABLES INITIALIZATION 
sections = {
    'CS': sections_cs,
    'IT': sections_it,
    'IS': sections_is
}

subjects = {
    'CS': subjects_CS_2,
    'IT': subjects_IT_2,
    'IS': subjects_IS_2
}



rooms = ['Room 320', 'Room 321', 'Room 322', 'Room 324', 'Room 326','Room 328', 'Room DOST-A', 'Room DOST-B', 'Room BODEGA-A', 'Room BODEGA-b']


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


import json

with open('output2.txt', 'w') as f:
    f.write(json.dumps(sections, indent=4) + '\n\n')
    f.write(json.dumps(subjects, indent=4) + '\n\n')
    f.write(str(rooms) + '\n\n')
    f.write(json.dumps(professors, indent=4) + '\n\n')
    f.write(json.dumps(time_slots, indent=4) + '\n\n')
     



