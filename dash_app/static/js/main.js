const ctx = document.getElementById('kpi1');
const myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                grid: {
                    display:false
                },
                beginAtZero: true,
                ticks:{
                    display: false
                }
            },
            x: {
                grid: {
                    display:false
                },
                ticks:{
                    display: false
                }
            }
        }
    }
});


const ctx3 = document.getElementById('kpi3');
const myChart3 = new Chart(ctx3, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue','Blue', 'Blue', 'Blue','Red', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue','Red', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue','Blue', 'Blue', 'Blue','Red', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
        datasets: [{
            label: 'data1',
            data: [12, 14, 19, 11, 18, 19, 25, 5, 30,12, 14, 19, 11, 18, 19, 25, 5, 30,12, 14, 19, 11, 18, 19, 25, 5, 30,12, 14, 19, 11, 18, 19, 25, 5, 30],
            backgroundColor: [
                'rgba(110, 227, 84, 0.8)',
            ],
            borderColor: [
                'rgba(110, 227, 84, 1)',
            ],
            borderWidth: 1
        },{
            label: 'data2',
            data: [18, 16, 11, 19, 12, 11, 5, 25, 0,18, 16, 11, 19, 12, 11, 5, 25, 0,18, 16, 11, 19, 12, 11, 5, 25, 0,18, 16, 11, 19, 12, 11, 5, 25, 0],
            backgroundColor: [
                'rgba(227, 222, 84, 0.8)',
            ],
            borderColor: [
                'rgba(227, 222, 84, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                stacked: true,
            },
            x: {
                beginAtZero: true,
                stacked: true,
            }
        }
    }
});



const ctx4 = document.getElementById('kpi4');
const myChart4 = new Chart(ctx4, {
    type: 'doughnut',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                grid: {
                    display:false
                },
                beginAtZero: true,
                ticks:{
                    display: false
                }
            },
            x: {
                grid: {
                    display:false
                },
                ticks:{
                    display: false
                }
            }
        }
    }
});




const ctx4_did = document.getElementById('kpi4_did');
const myChart4_did = new Chart(ctx4_did, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});




const ctx5 = document.getElementById('kpi5');
const myChart5 = new Chart(ctx5, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins:{
            legend:{
                display: false
            }
        }
    }
});


const ctx6 = document.getElementById('kpi6');
const myChart6 = new Chart(ctx6, {
    type: 'doughnut',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                grid: {
                    display:false
                },
                beginAtZero: true,
                ticks:{
                    display: false
                }
            },
            x: {
                grid: {
                    display:false
                },
                ticks:{
                    display: false
                }
            }
        }
    }
});



const ctx7 = document.getElementById('kpi7');
const myChart7 = new Chart(ctx7, {
    type: 'doughnut',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                grid: {
                    display:false
                },
                beginAtZero: true,
                ticks:{
                    display: false
                }
            },
            x: {
                grid: {
                    display:false
                },
                ticks:{
                    display: false
                }
            }
        }
    }
});




const ctx7_did = document.getElementById('kpi7_did');
const myChart7_did = new Chart(ctx7_did, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19],
            backgroundColor: [
                'rgba(255, 99, 132, 0.8)',
                'rgba(54, 162, 235, 0.8)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
