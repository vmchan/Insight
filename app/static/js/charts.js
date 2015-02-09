 $(document).ready(function(){

    var yearsdata = JSON.parse($('#yearsdata').html());

    var totalrevenuedata = JSON.parse($('#chart5data').html());

    var chart5 = c3.generate({
      bindto: '#chart5',
      size: {
        height: 350,
        width: 550
      },
      data: {
        x: 'x',
        columns: [
        yearsdata,
        totalrevenuedata
        ]
      },
      axis: {
        y: {
          min:0,
          label: { 
            text: 'Total Revenue (USD)',
            position: 'outer-middle'
          }, 
          tick: {
            format: function(d) { return "$" + d +'M'; }
          }
        }, 
        x: {
          label: { 
            text: 'Year',
            position: 'outer-center',
                  //padding: {top: 200, bottom: 200}
          }
        }
      },
      legend: {
        show: false
      }, 
      color: {
        pattern: ['#0db14b']
      },
      padding:{
        top:10, 
        bottom:10
      }
    });
            
    var totalexpensesdata = JSON.parse($('#chart2data').html());
    var chart2 = c3.generate({
      bindto: '#chart2',
      size: {
        height: 350,
        width: 550
      },
      data: {
        x: 'x',
        columns: [
        yearsdata,
        totalexpensesdata
        ]
      },
      axis: {
        y: {
          min:0,
          label: { // ADD
          text: 'Total Expenses (USD)',
          position: 'outer-middle'
          }, 
          tick: {
            format: function(d) { return "$" + d +'M'; }
          }
        }, 
        x: {
         label: { // ADD
           text: 'Year',
           position: 'outer-center'
         }
        }
      },
      legend: {
         show: false
      }, 
      color: {
        pattern: ['#b10d21']
      },
      padding:{
        top:10, 
        bottom:10
      }
    });
    
    var govgrantsdata = JSON.parse($('#chart3data').html());        
    var chart3 = c3.generate({
      bindto: '#chart3',
      size: {
        height: 350,
        width: 550
      },
      data: {
        x: 'x',
        columns: [
          yearsdata,
          govgrantsdata
          ]
      },
      axis: {
        y: {
          min:0,
          label: { // ADD
            text: 'Government Grants (USD)',
            position: 'outer-middle'
          }, 
          tick: {
            format: function(d) { return "$" + d +'M'; }
          }
        }, 
        x: {
          label: { // ADD
          text: 'Year',
          position: 'outer-center'
          }
        }
      },
      legend: {
        show: false
      }, 
      color: {
        pattern: ['#0db14b']
      },
      padding:{
        top:10, 
        bottom:10
      }
    });

    var wagesdata = JSON.parse($('#chart4data').html());
    var chart4 = c3.generate({
    bindto: '#chart4',
    size: {
      height: 350,
      width: 550
    },
    data: {
      x: 'x',
      columns: [
        yearsdata,
        wagesdata
      ]
    },
    axis: {
      y: {
        min:0,
        label: { // ADD
          text: 'Total Wages (USD)',
          position: 'outer-middle'
        }, 
        tick: {
                format: function(d) { return "$" + d +'M'; }
              }
      }, 
      x: {
        label: { // ADD
          text: 'Year',
          position: 'outer-center'
        }
      }
    },
    legend: {
      show: false
    }, 
    color: {
      pattern: ['#b10d21']
    },
    padding:{
      top:10, 
      bottom:10
    }
    });

    var assetsdata = JSON.parse($('#chartdata').html());
    var chart = c3.generate({
    bindto: '#chart',
    size: {
      height: 350,
      width: 550
    },
    data: {
      x: 'x',
      columns: [
        yearsdata,
        assetsdata
      ]
    },
    axis: {
      y: {
        min:0,
        label: { // ADD
          text: 'Total Assets (USD)',
          position: 'outer-middle'
        }, 
        tick: {
                format: function(d) { return "$" + d +'M'; }
              }
      }, 
      x: {
        label: { // ADD
          text: 'Year',
          position: 'outer-center'
        }
      }
    },
    legend: {
      show: false
    }, 
    color: {
      pattern: ['#0db14b']
    },
    padding:{
      top:10, 
      bottom:10
    }
    });
    
    var liabilitydata = JSON.parse($('#chart6data').html());
    var chart6 = c3.generate({
    bindto: '#chart6',
    size: {
      height: 350,
      width: 550
    },
    data: {
      x: 'x',
      columns: [
        yearsdata,
        liabilitydata
      ]
    },
    axis: {
      y: {
        min:0,
        label: { // ADD
          text: 'Other Liabilities (USD)',
          position: 'outer-middle'
        }, 
        tick: {
                format: function(d) { return "$" + d +'M'; }
              }
      }, 
      x: {
        label: { // ADD
          text: 'Year',
          position: 'outer-center'
        }
      }
    },
    legend: {
      show: false
    }, 
    color: {
      pattern: ['#b10d21']
    },
    padding:{
      top:10, 
      bottom:10
    }
    });

 });
