var columnDefs1 = [
    {headerName: "#", field: "CLASS_NUMBER", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs:0,
    }},
    {headerName: "Course Name", field: "COURSE", width: 120, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},
    {headerName: "Days", field: "DAYS", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},
    {headerName: "Time", field: "TIME", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},
    {headerName: "Location", field: "LOCATION", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},{headerName: "Instructor", field: "INSTRUCTOR", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }}
];

var gridOptions1 = {
    defaultColDef: {
        sortable: true,
        filter: true
    },
    columnDefs: columnDefs1,
    rowData: null,
    floatingFilter:true
};

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function() {
    var gridDiv1 = document.querySelector('#myGrid1');
    new agGrid.Grid(gridDiv1, gridOptions1);

    // do http request to get our sample data - not using any framework to keep the example self contained.
    // you will probably use a framework like JQuery, Angular or something else to do your HTTP calls.
    var httpRequest1 = new XMLHttpRequest();
    httpRequest1.open('GET', 'https://raw.githubusercontent.com/rosswelltiongco/CSULB_Class_Search/master/data.json');
    httpRequest1.send();
    httpRequest1.onreadystatechange = function() {
        if (httpRequest1.readyState === 4 && httpRequest1.status === 200) {
            var httpResult1 = JSON.parse(httpRequest1.responseText);
            gridOptions1.api.setRowData(httpResult1);
        }
    };
});