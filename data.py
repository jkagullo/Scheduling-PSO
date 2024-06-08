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
