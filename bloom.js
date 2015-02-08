// bloomberg stuff here
// usage: node historicalDataRequest.js
var request = require('request');
var fs = require('fs');

var host = 'http-api.openbloomberg.com';
var port = 443 ;

var options = {
    host: host,
    port: port,
    path: '/request/blp/refdata/HistoricalData',
    method: 'POST',
    key: fs.readFileSync('client.key'),
    cert: fs.readFileSync('client.crt'),
    ca: fs.readFileSync('bloomberg.crt')
};

var stocks = ["AAPL US Equity"];
stocks = [process.argv[2]];

var options = {
    url: 'https://' + host + '/request/blp/refdata/HistoricalData' ,
    json: true,
    body:{
      "securities": stocks,
      "fields": ["PX_LAST"],
      "startDate": "20120101",
      "endDate": "20130101",
      "periodicitySelection": "DAILY"
    },

    agentOptions: {
      key: fs.readFileSync('client.key'),
      cert: fs.readFileSync('client.crt'),
      ca: fs.readFileSync('bloomberg.crt')
    }
};

var stockPrices = [ ];

request.post(options, function(err, reponse, body) {
  console.log(body) ;
  var l = body.data[0].securityData.fieldData;
  var s = "";
  for (var i = 0; i < l.length; i++){
    stockPrices[i] = l[i].PX_LAST;
    s += l[i].PX_LAST + '\n';
  }

  fs.writeFile("prices.txt", s);
});


/*
var date = new Date();

date.getYear()


*/
