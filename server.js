var express = require('express');
var app = express();
var path = require("path");

var port = (8080);
var public = path.join(__dirname,'public/');

app.get('/',function(req,res){
    res.sendFile(public +"/socialGraph.html")
});

app.use('/',express.static(public));

app.listen(port);
console.log('Listening at port', port);
