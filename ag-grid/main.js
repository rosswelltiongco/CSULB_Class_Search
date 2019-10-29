var columnDefs = [
    {headerName: "Athlete", field: "athlete", width: 150, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs:0,
    }},
    {headerName: "Country", field: "country", width: 120, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},
    {headerName: "Year", field: "year", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }},
    {headerName: "Sport", field: "sport", width: 90, filter: 'agTextColumnFilter', filterParams:{
        filterOptions:['contains'],
        debounceMs: 0,
    }}
];

var gridOptions = {
    defaultColDef: {
        sortable: true,
        filter: true
    },
    columnDefs: columnDefs,
    rowData: null,
    floatingFilter:true
};

// setup the grid after the page has finished loading
document.addEventListener('DOMContentLoaded', function() {
    var gridDiv = document.querySelector('#myGrid');
    new agGrid.Grid(gridDiv, gridOptions);

    // do http request to get our sample data - not using any framework to keep the example self contained.
    // you will probably use a framework like JQuery, Angular or something else to do your HTTP calls.
    var httpRequest = new XMLHttpRequest();
    httpRequest.open('GET', 'https://raw.githubusercontent.com/ag-grid/ag-grid/master/packages/ag-grid-docs/src/olympicWinnersSmall.json');
    httpRequest.send();
    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState === 4 && httpRequest.status === 200) {
            var httpResult = JSON.parse(httpRequest.responseText);
            gridOptions.api.setRowData(httpResult);
        }
    };
});