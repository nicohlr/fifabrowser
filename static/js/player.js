var describe_attributes = {
}

window.onload = function () {
    Chart.defaults.global.defaultFontFamily = 'Raleway';
    Chart.defaults.global.defaultFontSize = 10;
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels:  ['Pace', 'Dribbling', 'Shooting', 'Defending', 'Passing', 'Physicality'],
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
                data: [90, 70, 90, 40, 80, 60],
            },
            ]
        },
        options: {
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
                    label: function(tooltipItem, data) {
                        return describe_attributes[data.labels[tooltipItem.index]];
                    }
                }
            }
        }
    });
}