var http = require('http');
var url = require('url');

var server = http.createServer(function(req, res) {

  var url_parse = url.parse(req.url, true);
  const execSync = require('child_process').execSync;

  console.log(req.url);

  switch (true) {
    case /\/up/.test(req.url):
      execSync('python3 /root/py/forward.py');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/control.html'
      })
      break;

    case /\/down/.test(req.url):
      execSync('python3 /root/py/reverse.py');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/control.html'
      })
      break;
    
    case /\/left/.test(req.url):
      execSync('');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/contrl.html'
      })

      break;

    case /\/right/.test(req.url):
      execSync('');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/control.html'
      })
      break;
  }

  res.end();
}).listen(8080);
