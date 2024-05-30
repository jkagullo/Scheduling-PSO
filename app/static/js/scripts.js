document.addEventListener('DOMContentLoaded', function() {
    changeTab();
});

function changeTab() {
    var nextButton = document.querySelectorAll('.next-back-button');

    nextButton.forEach(function(button) {
        button.addEventListener('click', function() {
            var buttonId = button.id;

            removeAllDisplayTab();
            if (buttonId === 'roomSchedNext' || buttonId === 'roomSchedBack') {
                document.getElementById('schedName').style.display = 'none';
                document.getElementById('roomSchedule').style.display = 'block';
                document.getElementById('progressBar').style.width = '40%';
            } 
            else if (buttonId === 'schedNameBack') {
                document.getElementById('roomSchedule').style.display = 'none';
                document.getElementById('schedName').style.display = 'block';
                document.getElementById('progressBar').style.width = '20%';
            }
            else if (buttonId === 'programNext') {
                document.getElementById('schedName').style.display = 'none';
                document.getElementById('programs').style.display = 'block';
                document.getElementById('progressBar').style.width = '60%';
            }
        });
    });
}

function removeAllDisplayTab() {
    document.getElementById('schedName').style.display = 'none';
    document.getElementById('roomSchedule').style.display = 'none';
}