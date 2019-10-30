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

ecs412 = ["TuTh 8-8:50AM", "TuTh 9-10:15AM", "MW 6-7:15PM", "F 3-5:30PM", "MW 9-10:15AM", "MW 12-1:15PM", "TuTh 10:30-11:45AM", "F 11-1:30PM", "TuTh 12-1:15PM", "MW 8:30-9:45PM", "MW 4-5:15PM", "TuTh 1:30-2:45PM", "TuTh 7-8:15PM", "TuTh 7-8:15PM"]
ecs416 = ["TuTh 1:30-2:45PM", "MW 11-12:15PM", "F 12-2:30PM", "MW 3-3:50PM", "MW 4-5:15PM", "TuTh 3-4:15PM", "TuTh 3-4:15PM", "TuTh 10:30-11:45AM", "TuTh 6-7:15PM", "MW 7:30-8:45PM", "TuTh 4:30-5:45PM", "TuTh 4:30-5:45PM", "TuTh 12-1:15PM", "MW 6-7:15PM", "TuTh 9-10:15AM", "TuTh 7:30-8:45PM", "TuTh 7:30-8:45PM"]

var x = minutesLeft(ecs412);
console.log(x);