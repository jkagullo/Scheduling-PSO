// new sched button
document.getElementById('createSchedule').addEventListener('click', function() {
    localStorage.clear();       // Clear local storage
    window.location.href = '/form';
})

document.getElementById('cancel-prof-modal-button').addEventListener('click', function() {
    document.getElementById('profModal').style.display = 'none';
})

document.getElementById('cancel-room-modal-button').addEventListener('click', function() {
    document.getElementById('roomModal').style.display = 'none';
})

function checkConflicts(data) {
    let conflicts = [];
    for (let i = 0; i < data.length; i++) {
        for (let j = 0; j < data.length; j++) {
            if (i !== j && ((data[i][2] === data[j][2] && data[i][3] === data[j][3]) || 
                (data[i][3] === data[j][3] && data[i][4] === data[j][4]))) {
                if (!conflicts.some(conflict => JSON.stringify(conflict) === JSON.stringify(data[i]))) {
                    conflicts.push(data[i]);
                }
            }
        }
    }

    // Sort by section
    conflicts.sort((a, b) => a[0] - b[0]);

    return conflicts;
}


function main(data, scheduleData) {
    var scheduledSections = Object.keys(data).length
    var totalSections = localStorage.getItem('totalSections');
    let conflicts = checkConflicts(scheduleData);

    if (conflicts.length === 0 && scheduledSections === totalSections) {
        document.getElementById('modal').style.display = 'none';
        return;
    }

    if (conflicts.length > 0) {
        document.getElementById('roomModal').style.display = 'flex';
        document.getElementById('insufficientRoomModal').style.display = 'flex';
        for (let i = 0; i < conflicts.length; i++) {
            var tbody = document.querySelector("#conflictTable tbody");

            var row = document.createElement("tr");

            var tdSection = document.createElement("td");
            tdSection.textContent = conflicts[i][0];
            row.appendChild(tdSection);

            var tdSubject = document.createElement("td");
            tdSubject.textContent = conflicts[i][1];
            row.appendChild(tdSubject);

            var tdProfessor = document.createElement("td");
            tdProfessor.textContent = conflicts[i][2];
            row.appendChild(tdProfessor);

            var tdTime = document.createElement("td");
            tdTime.textContent = conflicts[i][3];
            row.appendChild(tdTime);

            var tdRoom = document.createElement("td");
            tdRoom.textContent = conflicts[i][4];
            row.appendChild(tdRoom);

            tbody.appendChild(row);
        }
    }
    
    if (totalSections) {
        if (scheduledSections < totalSections) {
            document.getElementById('profModal').style.display = 'flex';
            document.getElementById('insufficientProfModal').style.display = 'flex';
            document.getElementById('totalSections').innerText = totalSections;
            document.getElementById('scheduledSections').innerText = scheduledSections;
        }
    }
}

fetch('/static/schedule.json')
    .then(response => response.json())
    .then(data => {
        let scheduleData = [];
        for (let section in data) {
            for (let entry of data[section]) {
                scheduleData.push(entry);
            }
        }
        main(data, scheduleData);
    })
    .catch(error => console.error('Error:', error));