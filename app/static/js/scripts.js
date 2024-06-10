





let schedName = '';
let roomSchedule = [];
let sections_cs = {
    1: [],
    2: [],
    3: [],
    4: []
}

let sections_it = {
    1: [],
    2: [],
    3: [],
    4: []
}

let sections_is = {
    1: [],
    2: [],
    3: [],
    4: []
}

sections = {
    'CS': sections_cs,
    'IT': sections_it,
    'IS': sections_is
}

let professors = {};

document.addEventListener('DOMContentLoaded', function() {
    handleButtonClick();
});

function changeTab(buttonId) {
    removeAllDisplayTab();
    if (buttonId === 'schedNameNext' || buttonId === 'schedNameBack') {
        document.getElementById('schedName').style.display = 'block';
        document.getElementById('progressBar').style.width = '25%';
    }
    else if (buttonId === 'roomSchedNext' || buttonId === 'roomSchedBack') {
        document.getElementById('roomSchedule').style.display = 'block';
        document.getElementById('progressBar').style.width = '75%';
    } 
    else if (buttonId === 'programNext' || buttonId === 'programBack') {
        document.getElementById('programs').style.display = 'block';
        document.getElementById('progressBar').style.width = '50%';
    }
    else if (buttonId === 'professorNext') {
        document.getElementById('professors').style.display = 'block';
        document.getElementById('progressBar').style.width = '100%';
    }
    // else if (buttonId === 'submitInfo') {
    //     document.querySelector('header').style.display = 'none';
    //     document.getElementById('modal').style.display = 'flex';
        
    //     // Temporary redirect to schedule page
    //     setTimeout(() => { window.location.href = '/schedule' }, 5000);
    // }
}

function removeAllDisplayTab() {
    document.getElementById('schedName').style.display = 'none';
    document.getElementById('roomSchedule').style.display = 'none';
    document.getElementById('programs').style.display = 'none';
    document.getElementById('professors').style.display = 'none';
}


function handleButtonClick() {
    var parentProfessorElement = document.getElementById('profInput');

    // Handle clicked event in Subject Container
    parentProfessorElement.addEventListener('click', function(event) {

        if (!event.target.matches('input[type="time"]'))
            event.preventDefault();

        if (event.target.matches('.add-button')) {
            var parentElement = event.target.parentNode.parentNode.parentNode;
            
            var newElementId = incrementId(parentElement);

            // Add the new element  
            if (parentElement.id.includes('addProfessorDetails')) {
                var length = parentElement.children.length;
                var lastChildElement = parentElement.children[length - 1];
                var removeAddButtonElement = lastChildElement.children[lastChildElement.children.length - 1];

                // Create new div
                var addProfDetailsDiv = document.createElement('div');
                addProfDetailsDiv.setAttribute('class', 'grid-2 add-subject-mg-top');

                // Remove the add button
                lastChildElement.removeChild(removeAddButtonElement);

                // Add new subject element
                var newSubjectHTML = `
                    <div class="subject-container">
                        <select name="subject" id="subject">
                            <option value="" selected>Any Subject</option>
                            <optgroup label="Computer Science">
                                <option value="CC103-M">Discrete Structures</option>
                                <option value="CS123-M">Linear Algebra</option>
                                <option value="CC201L-M">Information Management Lab</option>
                                <option value="CC202-M">Information Management Lec</option>
                                <option value="CC223-M">Applications Development and Emerging Technologies</option>
                                <option value="CS201L-M">Operating System Lab</option>
                                <option value="CS202-M">Operating System Lec</option>
                                <option value="CS221L-M">Programming Language Lab</option>
                                <option value="CS222-M">Programming Language Lec</option>
                                <option value="CS243-M">Design and Analysis of Algorithms</option>
                                <option value="CS261L-M">Networks and Communications Lab</option>
                                <option value="CS262-M">Networks and Communications Lec</option>
                                <option value="CC303-M">Methods of Research in Computing</option>
                                <option value="CS303-M">Automata Theory and Formal Language</option>
                                <option value="CS321L-M">Artificial Intelligence Lab</option>
                                <option value="CS322-M">Artificial Intelligence Lec</option>
                                <option value="CS343-M">Modeling and Simulation</option>
                                <option value="CS361L-M">Software Engineering 2 Lab</option>
                                <option value="CS362-M">Software Engineering 2 Lec</option>
                                <option value="CSE3-M">CS Elective 3</option>
                                <option value="CSE4-M">CS Elective 4</option>
                                <option value="CS403">Supervised Industrial Training</option>
                                <option value="CS423">Thesis Writing 2</option>
                            </optgroup>
                            <optgroup label="Information Technology">
                                <option value="CC103-M">Discrete Structures</option>
                                <option value="IT123-M">Human Computer Interaction</option>
                                <option value="MATHSTAT03-M">Probability and Statistics</option>
                                <option value="CC201L-M">Information Management Lab</option>
                                <option value="CC202-M">Information Management Lec</option>
                                <option value="CC223-M">Applications Development and Emerging Technologies</option>
                                <option value="IT201L-M">Programming Language Lab</option>
                                <option value="IT202-M">Programming Language Lec</option>
                                <option value="IT223-M">Quantitative Methods</option>
                                <option value="IT241L-M">Computer Networking 1 Lab</option>
                                <option value="IT242-M">Computer Networking 1 Lec</option>
                                <option value="IT261L-M">Multimedia Authoring & Production Lab</option>
                                <option value="IT262-M">Multimedia Authoring & Production Lec</option>
                                <option value="ITE1-M">IT Elective 1</option>
                                <option value="CC303-M">Methods of Research in Computing</option>
                                <option value="GEE11D-M">Living in the IT Era</option>
                                <option value="IT303-M">Systems Integration and Architecture 1</option>
                                <option value="IT323">Business Intelligence</option>
                                <option value="IT343-M">System Administration and Maintenance</option>
                                <option value="IT363-M">Information Assurance and Security 2</option>
                                <option value="ITE4-M">IT Elective 4</option>
                                <option value="IT406-M">Supervised Industrial Training</option>
                                <option value="IT423-M">IT Capstone & Research 2</option>
                            </optgroup>
                            <optgroup label="Information Security">
                                <option value="CC103-M">Discrete Structures</option>
                                <option value="IS123-M">Fundamentals of Information Systems</option>
                                <option value="MATHSTAT03-M">Probability and Statistics</option>
                                <option value="CC201L-M">Information Management Lab</option>
                                <option value="CC202-M">Information Management Lec</option>
                                <option value="CC223-M">Applications Development and Emerging Technologies</option>
                                <option value="IS203-M">Accounting and Financial Management</option>
                                <option value="IS223-M">Business Process Management</option>
                                <option value="IS243-M">IT Infrastructure and Network Technologies</option>
                                <option value="IS263-M">Business Intelligence</option>
                                <option value="ISE1-M">IS Elective 1</option>
                                <option value="CC303-M">Methods of Research in Computing</option>
                                <option value="IS303-M">Information Assurance and Security 2</option>
                                <option value="IS323-M">Enterprise Architecture</option>
                                <option value="IS343-M">IS Strategy, Management and Acquisition</option>
                                <option value="IS363-M">IS Project Management 2</option>
                                <option value="IS383-M">Evaluation and Business Performance</option>
                                <option value="ISE4-M">IS Elective 4</option>
                                <option value="IS406-M">Supervised Industrial Training</option>
                                <option value="IS423-M">IS Capstone Project 2</option>
                            </optgroup>
                            <optgroup label="Computer Programming">
                                <option value="CC141L-M">Computer Programming 2 Lab</option>
                                <option value="CC142-M">Computer Programming 2 Lec</option>
                            </optgroup>
                            <optgroup label="General Education Courses">
                                <option value="GEC2-M">Readings in Philippine History</option>
                                <option value="GEC3-M">The Contemporary World</option>
                                <option value="GEC5-M">Purposive Communication</option>
                                <option value="MATHA35-M">Differential and Integral Calculus</option>
                                <option value="NSTP2-M">National Service Training Program 2</option>
                                <option value="PE2-M">Rhythmic Activities</option>
                                <option value="PE3-M">Individual and Dual Sports</option>
                                <option value="PE4-M">Team Sports</option>
                            </optgroup>
                        </select>
                        <button class="delete-subject-button mg-top">delete</button>
                    </div>  
                    <div class="add-button-container add-subject">
                        <img src="${addIconUrl}"/>
                        <button type="button" class="add-button">add</button>
                    </div>
                `;
                addProfDetailsDiv.innerHTML = newSubjectHTML;
                parentElement.appendChild(addProfDetailsDiv);
            }

            else if (parentElement.classList[0] === 'add-prof-button') {
                var grandParentElement = parentElement.parentNode;
                var length = grandParentElement.children.length;
                var lastChildElement = grandParentElement.children[length - 1];

                // Remove the add button
                grandParentElement.removeChild(lastChildElement);

                // Create new div of add professor details
                var addProfessorDetailsDiv = document.createElement('div');
                addProfessorDetailsDiv.setAttribute('id', newElementId);
                addProfessorDetailsDiv.setAttribute('class', 'prof-details');

                var newProfessorDetailsHTML = `
                <div class="grid-1">
                    <div class="prof-name">
                        <div class="input-prof-name">
                            <img src="${profIconUrl}">
                            <input type="text" placeholder="Professor Name" pattern="^[a-zA-Z\\s]*$" required>
                            <select name="preferred-time">
                                <option value="" selected>Anytime</option>
                                <option value="AM">AM</option>
                                <option value="PM">PM</option>
                            </select>
                        </div>
                    </div>
                    <button class="delete-prof-container-button">delete</button>
                </div>
                <div class="grid-2">
                    <label>Preferred Subject</label>
                    <div class="subject-container">
                        <select name="subject" id="subject">
                            <option value="" selected>Any Subject</option>
                            <optgroup label="Computer Science">
                                <option value="CC103-M">Discrete Structures</option>
                                <option value="CS123-M">Linear Algebra</option>
                                <option value="CC201L-M">Information Management Lab</option>
                                <option value="CC202-M">Information Management Lec</option>
                                <option value="CC223-M">Applications Development and Emerging Technologies</option>
                                <option value="CS201L-M">Operating System Lab</option>
                                <option value="CS202-M">Operating System Lec</option>
                                <option value="CS221L-M">Programming Language Lab</option>
                                <option value="CS222-M">Programming Language Lec</option>
                                <option value="CS243-M">Design and Analysis of Algorithms</option>
                                <option value="CS261L-M">Networks and Communications Lab</option>
                                <option value="CS262-M">Networks and Communications Lec</option>
                                <option value="CC303-M">Methods of Research in Computing</option>
                                <option value="CS303-M">Automata Theory and Formal Language</option>
                                <option value="CS321L-M">Artificial Intelligence Lab</option>
                                <option value="CS322-M">Artificial Intelligence Lec</option>
                                <option value="CS343-M">Modeling and Simulation</option>
                                <option value="CS361L-M">Software Engineering 2 Lab</option>
                                <option value="CS362-M">Software Engineering 2 Lec</option>
                                <option value="CSE3-M">CS Elective 3</option>
                                <option value="CSE4-M">CS Elective 4</option>
                                <option value="CS403">Supervised Industrial Training</option>
                                <option value="CS423">Thesis Writing 2</option>
                            </optgroup>
                            <optgroup label="Information Technology">
                                <option value="CC103-M">Discrete Structures</option>
                                <option value="IT123-M">Human Computer Interaction</option>
                                <option value="MATHSTAT03-M">Probability and Statistics</option>
                                <option value="CC201L-M">Information Management Lab</option>
                                <option value="CC202-M">Information Management Lec</option>
                                <option value="CC223-M">Applications Development and Emerging Technologies</option>
                                <option value="IT201L-M">Programming Language Lab</option>
                                <option value="IT202-M">Programming Language Lec</option>
                                <option value="IT223-M">Quantitative Methods</option>
                                <option value="IT241L-M">Computer Networking 1 Lab</option>
                                <option value="IT242-M">Computer Networking 1 Lec</option>
                                <option value="IT261L-M">Multimedia Authoring & Production Lab</option>
                                <option value="IT262-M">Multimedia Authoring & Production Lec</option>
                                <option value="ITE1-M">IT Elective 1</option>
                                <option value="CC303-M">Methods of Research in Computing</option>
                                <option value="GEE11D-M">Living in the IT Era</option>
                                <option value="IT303-M">Systems Integration and Architecture 1</option>
                                <option value="IT323">Business Intelligence</option>
                                <option value="IT343-M">System Administration and Maintenance</option>
                                <option value="IT363-M">Information Assurance and Security 2</option>
                                <option value="ITE4-M">IT Elective 4</option>
                                <option value="IT406-M">Supervised Industrial Training</option>
                                <option value="IT423-M">IT Capstone & Research 2</option>
                            </optgroup>
                            <optgroup label="Information Security">
                                <option value="CC103-M">Discrete Structures</option>
                                <option value="IS123-M">Fundamentals of Information Systems</option>
                                <option value="MATHSTAT03-M">Probability and Statistics</option>
                                <option value="CC201L-M">Information Management Lab</option>
                                <option value="CC202-M">Information Management Lec</option>
                                <option value="CC223-M">Applications Development and Emerging Technologies</option>
                                <option value="IS203-M">Accounting and Financial Management</option>
                                <option value="IS223-M">Business Process Management</option>
                                <option value="IS243-M">IT Infrastructure and Network Technologies</option>
                                <option value="IS263-M">Business Intelligence</option>
                                <option value="ISE1-M">IS Elective 1</option>
                                <option value="CC303-M">Methods of Research in Computing</option>
                                <option value="IS303-M">Information Assurance and Security 2</option>
                                <option value="IS323-M">Enterprise Architecture</option>
                                <option value="IS343-M">IS Strategy, Management and Acquisition</option>
                                <option value="IS363-M">IS Project Management 2</option>
                                <option value="IS383-M">Evaluation and Business Performance</option>
                                <option value="ISE4-M">IS Elective 4</option>
                                <option value="IS406-M">Supervised Industrial Training</option>
                                <option value="IS423-M">IS Capstone Project 2</option>
                            </optgroup>
                            <optgroup label="Computer Programming">
                                <option value="CC141L-M">Computer Programming 2 Lab</option>
                                <option value="CC142-M">Computer Programming 2 Lec</option>
                            </optgroup>
                            <optgroup label="General Education Courses">
                                <option value="GEC2-M">Readings in Philippine History</option>
                                <option value="GEC3-M">The Contemporary World</option>
                                <option value="GEC5-M">Purposive Communication</option>
                                <option value="MATHA35-M">Differential and Integral Calculus</option>
                                <option value="NSTP2-M">National Service Training Program 2</option>
                                <option value="PE2-M">Rhythmic Activities</option>
                                <option value="PE3-M">Individual and Dual Sports</option>
                                <option value="PE4-M">Team Sports</option>
                            </optgroup>
                        </select>
                        </select>
                        <div class="temp-container"></div>
                    </div>  
                    <div class="add-button-container add-subject">
                        <img src="${addIconUrl}"/>
                        <button type="button" class="add-button">add</button>
                    </div>
                </div>
                `;
                addProfessorDetailsDiv.innerHTML += newProfessorDetailsHTML;

                // Create new div of add professor button
                var addProfessorButton = document.createElement('div');
                addProfessorButton.setAttribute('class', 'add-prof-button prof-add')

                var newAddProfButtonHTML = `
                    <div class="grid-1">
                        <div class="add-button-container add-prof">
                            <img src="${addIconUrl}"/>
                            <button type="button" id="addProfessorButton" class="add-button">add professor</button>
                        </div>
                    </div>
                `;
                addProfessorButton.innerHTML += newAddProfButtonHTML;

                // Append the new nodes
                grandParentElement.appendChild(addProfessorDetailsDiv);
                grandParentElement.appendChild(addProfessorButton);
            }
        }

        else if (event.target.matches('.delete-subject-button')) {
            var parentElement = event.target.parentNode;
            
            // Remove the element
            parentElement.remove();
        }
        else if (event.target.matches('.delete-prof-container-button')) {
            var parentElement = event.target.parentNode.parentNode;
            
            // Remove the element
            parentElement.remove();
        }
    });
}



function incrementId(parentElement) {
    if (parentElement.classList[0] === 'add-prof-button') {
        var searchString = "addProfessorDetails";
        var grandParentElement = parentElement.parentNode;
        var length = grandParentElement.children.length;

        // Get the last child element (add prof container)
        var lastChildAddProfContainer = grandParentElement.children[length - 2];

        if (lastChildAddProfContainer.id.includes('addProfessorDetails')) {
            var addProfContainerId = lastChildAddProfContainer.id;
            var lastChar = addProfContainerId.slice(searchString.length, addProfContainerId.length);

            // Increment the last character of the id
            var newChar = parseInt(lastChar) + 1;

            // Create new id
            var newId = addProfContainerId.slice(0, searchString.length) + newChar;
        }
        return newId;
    }
    return;
}


document.getElementById('schedNameForm').addEventListener('submit', function(e) {
    e.preventDefault();
    schedName = document.getElementById('schedNameInput').value;
});

document.getElementById('sectionForm').addEventListener('submit', function(e) {
    e.preventDefault();

    function addSections(input, index, program) {
        let sectionLetter = 'A';
        if (program === 'CS') {
            for (let i = 0; i < input.value; i++) {
                let section = 'Section ' + index + sectionLetter + '-' + program;

                if (!(sections_cs[index].includes(section))) {
                    sections_cs[index].push(section);
                }
                // increase letter (charcode) by 1
                sectionLetter = String.fromCharCode(sectionLetter.charCodeAt(0) + 1);
            }
            // Remove excess sections if necessary
            while (sections_cs[index].length > input.value) {
                sections_cs[index].pop();
            }
        }
        else if (program === 'IT') {
            if (index === 6)  index = 1;
            else if (index === 7)  index = 2;
            else if (index === 8)  index = 3;
            else if (index === 9)  index = 4;

            for (let i = 0; i < input.value; i++) {
                let section = 'Section ' + index + sectionLetter + '-' + program;

                if (!(sections_it[index].includes(section))) {
                    sections_it[index].push(section);
                }
                // increase letter (charcode) by 1
                sectionLetter = String.fromCharCode(sectionLetter.charCodeAt(0) + 1);
            }
            // Remove excess sections if necessary
            while (sections_it[index].length > input.value) {
                sections_it[index].pop();
            }
        }
        else if (program === 'IS') {
            if (index === 11) index = 1;
            else if (index === 12) index = 2;
            else if (index === 13) index = 3;
            else if (index === 14) index = 4;

            for (let i = 0; i < input.value; i++) {
                let section = 'Section ' + index + sectionLetter + '-' + program;

                if (!sections_is[index].includes(section)) {
                    sections_is[index].push(section);
                }
                // increase letter (charcode) by 1
                sectionLetter = String.fromCharCode(sectionLetter.charCodeAt(0) + 1);
            }
            // Remove excess sections if necessary
            while (sections_is[index].length > input.value) {
                sections_is[index].pop();
            }
        }
    }

    function getInputValues() {
        var inputs = document.querySelectorAll('.section-input input')
        
        inputs.forEach(function(input, index) {
            if (input.value !== '') {
                if (index >= 1 && index <= 4) {
                    addSections(input, index, 'CS');
                }
                else if (index >= 6 && index <= 9) {
                    addSections(input, index, 'IT');
                }
                else if (index >= 11 && index <= 14) {
                    addSections(input, index, 'IS');
                }
            }
        })
    }
    getInputValues();
});

document.getElementById('roomScheduleForm').addEventListener('submit', function(e) {
    e.preventDefault();
    numRooms = document.getElementById('roomInput').value;
    numRooms = parseInt(numRooms);

    for (let i = 0; i < numRooms; i++) {
        let roomNumber = String(i).padStart(3, '0');

        if (!(roomSchedule.includes(roomNumber)))
            roomSchedule.push('Room ' + roomNumber);
    }

    // Remove duplicates
    roomSchedule = [...new Set(roomSchedule)];

    console.log(roomSchedule);
});

document.getElementById('professorForm').addEventListener('submit', function(e) {
    e.preventDefault();

    let professorDetails = document.querySelectorAll('.prof-details');
    professors = {};

    professorDetails.forEach(function(professorDetail) {
        let inputElements = professorDetail.querySelectorAll('input, select');
        let professorName = '';

        inputElements.forEach(function(inputElement) {
            if (inputElement.tagName === 'INPUT') {
                professorName = inputElement.value;
                professors[professorName] = {};
                professors[professorName]['preferred_subjects'] = [];
            }
            else if(inputElement.tagName === 'SELECT') {
                if (inputElement.name === 'preferred-time')
                    professors[professorName]['preferred_time'] = inputElement.value.toUpperCase();
                else if (inputElement.name === 'subject')
                    professors[professorName]['preferred_subjects'].push(inputElement.value.toUpperCase());
            }
        });

        // Display the pre-loading modal
        document.querySelector('header').style.display = 'none';
        document.getElementById('professors').style.display = 'none';
        document.getElementById('modal').style.display = 'flex';

        $.ajax({
            url: '/receive_data',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ sections, roomSchedule, professors, schedName }),
            success: function(response) {
                window.location.href = '/schedule';
            },
            error: function(error) {
                document.querySelector('header').style.display = 'flex';
                document.getElementById('modal').style.display = 'none';
                document.getElementById('professors').style.display = 'block';
                document.getElementById('progressBar').style.width = '100%';
                console.error('Error:', error);
            }
        })
    });
});


function calculateRoomsNeeded(sections) {
    let totalSections = 0;

    for (let program in sections) {
        for (let year in sections[program]) {
            totalSections += sections[program][year].length;
        }
    }
    let roomsMinimumNeeded = Math.ceil(totalSections / 2);

    return roomsMinimumNeeded;
}


var nextButton = document.querySelectorAll('.next-back-button');
nextButton.forEach(function(button) {
    button.addEventListener('click', function(e) {
        
        var buttonId = button.id;

        if (buttonId.includes('Back')) {
            e.preventDefault();
            changeTab(buttonId);
        }
        else if (buttonId.includes('Next')) {
            var form = document.getElementById(buttonId).closest('form');
            if (form.checkValidity()) {
                // Trigger form submission programmatically
                form.dispatchEvent(new Event('submit'));

                changeTab(buttonId);
            } else {
                console.log('Form is not valid');
            }
        }
    });
});


// Number of rooms input validation based on number of sections
let roomInput = document.getElementById('roomInput');

roomInput.addEventListener('input', function() {
    let minRoomsNeeded = calculateRoomsNeeded(sections); // Assuming you have this function from previous conversation

    if (this.value < minRoomsNeeded) {
        this.setCustomValidity(`Minimum number of rooms needed is ${minRoomsNeeded}`);
    } else {
        this.setCustomValidity('');
    }
    this.reportValidity();
});

