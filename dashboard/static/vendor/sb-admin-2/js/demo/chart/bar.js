'use strict'
// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

const fbRootURL = "https://www.facebook.com/profile.php?id="

// Bar Chart
const domElement = document.getElementById("maliciousUsersChart");
console.log(top20MostMaliciousUsers)
const chartConfig = {
  type: 'bar',
  data: {
    labels: top20MostMaliciousUsers.map((user) => user.user_id),
    datasets: [{
      label: "Malicious Score ",
      backgroundColor: "#4e73df",
      hoverBackgroundColor: "#2e59d9",
      borderColor: "#4e73df",
      data: top20MostMaliciousUsers.map((user) => user.malicious_score),
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 20
        },
        maxBarThickness: 25,
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 50,
          maxTicksLimit: 5,
          padding: 10,
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
  	onClick: barChartEventClick,
    tooltips: {
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function(tooltipItem, chart) {
          return `${chart.datasets[tooltipItem.datasetIndex].label}: ${tooltipItem.value}` || '';
        }
      }
    },
  }
}
const myBarChart = new Chart(domElement, chartConfig);

function barChartEventClick(event){
	const activeElement = myBarChart.getElementAtEvent(event);
	if(activeElement[0]){
		const [lastItem] = chartConfig.data.labels[activeElement[0]._index].split(" ").slice(-1)
		//	Thanks to: https://stackoverflow.com/a/37123117
		let profileURL = fbRootURL + lastItem;
		openInNewTab(profileURL)
	}
}

function openInNewTab(href) {
  Object.assign(document.createElement('a'), {
    target: '_blank',
    href: href,
  }).click();
}