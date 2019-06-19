function mean(numbers) {
    var total = 0, i;
    for (i = 0; i < numbers.length; i += 1) {
        total += numbers[i];
    }
    return total / numbers.length;
}

var inner_attributes = {
    'Pace': ['Acceleration: ' + attributes['Acceleration'], 'Sprint speed: ' + attributes['SprintSpeed']],
    'Dribbling': ['Agility: ' + attributes['Agility'], 'Balance: ' + attributes['Balance'], 'Ball control: ' + attributes['BallControl'], 'Composure: ' + attributes['Composure'], 'Dribbling: ' + attributes['Dribbling'], 'Reactions: ' + attributes['Reactions']],
    'Shooting': ['Finishing: ' + attributes['Finishing'], 'Long shots: ' + attributes['LongShots'], 'Penalties: ' + attributes['Penalties'], 'Positioning: ' + attributes['Positioning'], 'Shot power: ' + attributes['ShotPower'], 'Volleys: ' + attributes['Volleys']],
    'Defending': ['Heading: ' + attributes['HeadingAccuracy'], 'Interceptions: ' + attributes['Interceptions'], 'Marking: ' + attributes['Marking'], 'Sliding tackle: ' + attributes['SlidingTackle'], 'Standing tackle: ' + attributes['StandingTackle']],
    'Passing': ['Crossing: ' + attributes['Crossing'], 'Curve: ' + attributes['Curve'], 'Free kick: ' + attributes['FKAccuracy'], 'Long passing: ' + attributes['LongPassing'], 'Short passing: ' + attributes['ShortPassing'], 'Vision: ' + attributes['Vision']],
    'Physicality': ['Aggression: ' + attributes['Aggression'], 'Jumping: ' + attributes['Jumping'], 'Stamina: ' + attributes['Stamina'], 'Strength: ' + attributes['Strength']]
};

if (attributes['Position'] === 'GK') {
    var labels_attributes = ['Diving', 'Reflexes', 'Handling', 'Speed', 'Kicking', 'Positioning'];
    var global_attributes = [
        Math.round([attributes['GKDiving']]),
        Math.round([attributes['GKReflexes']]),
        Math.round([attributes['GKHandling']]),
        Math.round(mean([attributes['Acceleration'], attributes['SprintSpeed']])),
        Math.round([attributes['GKKicking']]),
        Math.round([attributes['GKPositioning']]),
    ];
}
else {
    var labels_attributes = ['Pace', 'Dribbling', 'Shooting', 'Defending', 'Passing', 'Physicality'];
    var global_attributes = [
        Math.round(mean([attributes['Acceleration'], attributes['SprintSpeed']])),
        Math.round(mean([attributes['Agility'], attributes['Balance'], attributes['BallControl'], attributes['Composure'], attributes['Dribbling'], attributes['Reactions']])),
        Math.round(mean([attributes['Finishing'], attributes['LongShots'], attributes['Penalties'], attributes['Positioning'], attributes['ShotPower'], attributes['Volleys']])),
        Math.round(mean([attributes['HeadingAccuracy'], attributes['Interceptions'], attributes['Marking'], attributes['SlidingTackle'], attributes['StandingTackle']])),
        Math.round(mean([attributes['Crossing'], attributes['Curve'], attributes['FKAccuracy'], attributes['LongPassing'], attributes['ShortPassing'], attributes['Vision']])),
        Math.round(mean([attributes['Aggression'], attributes['Jumping'], attributes['Stamina'], attributes['Strength']])),
    ];
}

$('.help').qtip({
    content: "You can hover the points of the radar chart to have detailled statistics on this player.<br><br>Grades displayed are just the mean of corresponding inner attributes. Therefore, it may exist some differences between displayed grades and the official grades given on FUT cards. ",
    style: { classes: 'qtip-bootstrap' },
    position: {
        my: "top left",
        at: "bottom right",
        target: $(".help"),
    },
    show: {
        delay: 300,
        solo: true
    }
});

window.onload = function () {
    Chart.defaults.global.defaultFontFamily = 'Raleway';
    Chart.defaults.global.defaultFontSize = 10;
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels_attributes,
            datasets: [{
                label: "Player's statistics",
                backgroundColor:
                    'rgba(255, 0, 104, 0.2)',
                borderColor:
                    'rgba(255, 0, 104, 0.6)',
                pointBackgroundColor:
                    'rgba(255, 0, 104, 0.6)',
                pointBorderColor:
                    'rgba(255, 0, 104, 0.6)',
                pointRadius: 8,
                pointHoverRadius: 10,
                data: global_attributes,
            },
            ]
        },
        options: {
            legend: {
                display: false
            },
            responsive: true,
            maintainAspectRatio: false,
            scale: {
                ticks: {
                    beginAtZero: true,
                    max: 100,
                    min: 0,
                    stepSize: 10
                }
            },
            tooltips: {
                displayColors: false,
                titleFontSize: 12,
                bodyFontSize: 10,
                enabled: true,
                callbacks: {
                    title: function(tooltipItem, data) {
                        console.log(tooltipItem);
                        console.log(data);
                        return data.labels[tooltipItem[0].index] + ': ' + data.datasets[0].data[tooltipItem[0].index];
                    },
                    label: function(tooltipItem, data) {
                        return inner_attributes[data.labels[tooltipItem.index]];
                    }
                }
            }
        }
    });

    if (attributes['Overall'] >= 80) {
        $('.overall').css('background', '#1A7E52')
    }
    else if (70<=attributes['Overall'] && attributes['Overall']<80) {
        $('.overall').css('background', '#9FBE32')
    }
    else if (60<=attributes['Overall'] && attributes['Overall']<70) {
        $('.overall').css('background', '#FECF45')
    }
    else if (50<=attributes['Overall'] && attributes['Overall']<60) {
        $('.overall').css('background', '#EB802D')
    }
    else {
        $('.overall').css('background', '#D13E20')
    }

    if (attributes['Potential'] >= 80) {
        $('.potential').css('background', '#1A7E52')
    }
    else if (70<=attributes['Potential'] && attributes['Potential']<80) {
        $('.potential').css('background', '#9FBE32')
    }
    else if (60<=attributes['Potential'] && attributes['Potential']<70) {
        $('.potential').css('background', '#FECF45')
    }
    else if (50<=attributes['Potential'] && attributes['Potential']<60) {
        $('.potential').css('background', '#EB802D')
    }
    else {
        $('.potential').css('background', '#D13E20')
    }
}