var http = require('http');
var url = require('url');

var server = http.createServer(function(req, res) {
  var url_parse = url.parse(req.url, true);
  console.log(url_parse);

  console.log(url_parse.query.dyu);

 const execSync = require('child_process').execSync;
 const result =  execSync('python3 /root/py/2test.py ' + url_parse.query.dyu);

  res.end();
}).listen(8080);
