var http = require('http');
var url = require('url');

var server = http.createServer(function(req, res) {

  var url_parse = url.parse(req.url, true);
  console.log(url_parse.query.dyu);
  const execSync = require('child_process').execSync;
  const exec = require('child_process').exec;

  console.log(req.url);

  switch (true) {
    case /\/upAndDown.*/.test(req.url):
      execSync('python3 /root/py/upAndDown.py ' + url_parse.query.dyu);
      break;

    case /\/around.*/.test(req.url):
      execSync('python3 /root/py/around.py ' + url_parse.query.dyu);
      break;
    
    case /\/start-motion\?/.test(req.url):
      execSync('/usr/bin/motion');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })
      break;

    case /\/stop-motion\?/.test(req.url):
      execSync('sh /data/nodejs/stop-motion.sh');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })
      break;

    case /\/up/.test(req.url):
      execSync('python3 /root/py/forward.py');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })
      break;

    case /\/down/.test(req.url):
      execSync('python3 /root/py/reverse.py');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })
      break;

    case /\/left/.test(req.url):
      execSync('python3 /root/py/forleft.py');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })

      break;

    case /\/right/.test(req.url):
      execSync('python3 /root/py/forright.py');
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })
      break;
    
    case /\/moter.*/.test(req.url):
      exec('python3 /root/py/moter.py ' + url_parse.query.time);
      res.writeHead(302, {
         'Location': 'http://192.168.1.200/'
      })
      break;
  }

  res.end();
}).listen(8080);
