function getToday() {
    var offset = -7
    d = new Date();   
  
    utc = d.getTime() + (d.getTimezoneOffset() * 60000);
  
    nd = new Date(utc + (3600000*offset));
  
    var n = nd.getDay()
    
    switch(n) {
    case 0:
      return "Su";
      break;
    case 1:
      return "M";
      break;
    case 2:
      return "Tu";
      break;
    case 3:
      return "W";
      break;
    case 4:
      return "Th";
      break;
    case 5:
      return "F";
      break;
    case 6:
      return "Sa";
      break;
    default:
      return "NA";
      // code block
    }
  }
  
  function getTime() {
      var offset = -7
      d = new Date();   
      
      utc = d.getTime() + (d.getTimezoneOffset() * 60000);
     
      nd = new Date(utc + (3600000*offset));
  
      var hour = nd.getHours();
      var minutes = nd.getMinutes();
      //return 630;
      return hour * 60 + minutes;
  }
  
  function convertTime(time) {
        var time = String(time);
        //morningCase = 'TuTh 10:30-11:45AM' // 630-745
        let timeRange = String(time.split(" ")[1]);
        let firstTime = timeRange.split("-")[0];
        let secondTime = timeRange.split("-")[1];

        // Populate 00 for convenience
        if (!firstTime.includes(':')){
            firstTime += ":00";
        }
        if (!secondTime.includes(':')){
            secondTime += ":00";
        }

        var firstHour = parseInt(firstTime.split(":")[0]);
        var firstMinutes = parseInt(firstTime.split(":")[1]);

        var secondHour = parseInt(secondTime.split(":")[0]);
        var secondMinutes = parseInt(secondTime.split(":")[1]);
        
        var convertedSecondTime = secondHour * 60 + secondMinutes;
        if (secondTime.includes('PM')){
            convertedSecondTime += 720
        }
        if (convertedSecondTime >= 1440){
            convertedSecondTime -= 720;
        }
        
        var convertedFirstTime = firstHour * 60 + firstMinutes;
        if (secondTime.includes('PM')){
            convertedFirstTime += 720;
        }
        if (convertedFirstTime >= 1440){
            convertedFirstTime -= 720;
        }
        if (convertedFirstTime > convertedSecondTime){
            convertedFirstTime -= 720;
        }

        var converted = convertedFirstTime.toString() +"-" + convertedSecondTime.toString()
        return converted;
}

function minutesLeft(classroomTimes){
    var minutesLeft = 999999;
    for (var i = 0; i < classroomTimes.length; i++){
        var time = classroomTimes[i];
        console.log(time.slice(0,-2));
        if (time.slice(0,-2).includes(getToday())){
            var startTime = convertTime(time).split('-')[0];
            var endTime = convertTime(time).split('-')[1];
            if (parseInt(startTime) < getTime() && getTime() < parseInt(endTime)){
                minutesLeft = parseInt(endTime) - getTime();
                return - minutesLeft;
            }
            var newTimeLeft = parseInt(startTime) - getTime();
            if ((newTimeLeft < minutesLeft) && (newTimeLeft > 0)){
                minutesLeft = newTimeLeft;
            }
        }
    }  
    return minutesLeft;
}


var columnDefs = [
    {headerName: "LOCATION", field: "LOCATION", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs:0, 
    }},
    /*
    {headerName: "TIMES", field: "TIMES", width: 120, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},
    */
  {headerName: "STATUS", 
        valueGetter: function(params) {
            var mins = minutesLeft(params.data.TIMES);
            if (mins > 0) {
              return "UNOCCUPIED";
            }
          else{
            return "OCCUPIED";
          }
        }},
  {headerName: "DURATION (mins)", colId: 'a&b',
        valueGetter: function(params) {
          var mins = minutesLeft(params.data.TIMES);
          if (mins > 1500) return "REST OF DAY";
          else if (mins > 0) return mins;
          else return - mins;
        }},
];

var gridOptions = {
    defaultColDef: {
        sortable: true,
        filter: true
    },
    columnDefs: columnDefs,
    rowData: null,
    floatingFilter:true,
  
};

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function() {
    var gridDiv = document.querySelector('#myGrid');
    new agGrid.Grid(gridDiv, gridOptions);

    // do http request to get our sample data - not using any framework to keep the example self contained.
    // you will probably use a framework like JQuery, Angular or something else to do your HTTP calls.
    var httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', 'https://raw.githubusercontent.com/rosswelltiongco/CSULB_Class_Search/master/schedule_data.json');
    httpRequest.send();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {
            var httpResult = JSON.parse(httpRequest.responseText);
            gridOptions.api.setRowData(httpResult);
        }
    };
});