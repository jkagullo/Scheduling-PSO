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
        document.getElementById('progressBar').style.width = '50%';
    } 
    else if (buttonId === 'programNext' || buttonId === 'programBack') {
        document.getElementById('programs').style.display = 'block';
        document.getElementById('progressBar').style.width = '75%';
    }
    else if (buttonId === 'professorNext') {
        document.getElementById('professors').style.display = 'block';
        document.getElementById('progressBar').style.width = '100%';
    }
    else if (buttonId === 'submitInfo') {
        document.querySelector('header').style.display = 'none';
        document.getElementById('modal').style.display = 'flex';
        
        // Temporary redirect to schedule page
        setTimeout(() => { window.location.href = '/schedule' }, 5000);
    }
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
        event.preventDefault();

        console.log(event.target);
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
                            <option value="" selected disabled>Select a subject</option>
                            <option value="artifical-intelligence">Artificial Intelligence</option>
                            <option value="automata">Automata</option>
                            <option value="decision-theory">Decision Theory</option>
                            <option value="data-analytics">Data Analytics</option>
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
                            <input type="text" placeholder="Professor Name">
                        </div>
                    </div>
                    <button class="delete-prof-container-button">delete</button>
                </div>
                <div class="grid-2">
                    <label>Preferred Subject</label>
                    <div class="subject-container">
                        <select name="subject" id="subject">
                                <option value="" selected disabled>Select a subject</option>
                                <option value="artifical-intelligence">Artificial Intelligence</option>
                                <option value="automata">Automata</option>
                                <option value="decision-theory">Decision Theory</option>
                                <option value="data-analytics">Data Analytics</option>
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
});

document.getElementById('roomScheduleForm').addEventListener('submit', function(e) {
    e.preventDefault();
});

document.getElementById('sectionForm').addEventListener('submit', function(e) {
    e.preventDefault();
});

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

