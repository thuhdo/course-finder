google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBarColors);

function drawBarColors(dataForBar) {
    if(dataForBar != ''){
      var data = google.visualization.arrayToDataTable(dataForBar[0]);
    }
    else{
    var data = google.visualization.arrayToDataTable([['Time', 'Amount of Ticket'], ['2019-1', 2], ['2019-2', 5], ['2019-3', 2], ['2019-4', 2], ['2020-2', 3]]);
    }		
    var options = {
    title: 'Amount of ticket sold',
    chartArea: {width: '50%'},
    colors: ['#b0120a', '#ffab91'],
    hAxis: {
      title: 'Sold',
      minValue: 0
    },
    vAxis: {
      title: 'Time'
    }
    };
    var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}