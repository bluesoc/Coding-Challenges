# Mock Backend JSON Server Script

require 'webrick'
require 'json'

# SERVER PORT
PORT=8081

# JSON RESPONSE
data = [{"hostname": "ngix-backend", "cpu": 32, "ram": 64},{"hostname": "web-server-s1", "cpu": 128, "ram": 256},{"hostname": "ngix-backend", "cpu": 32, "ram": 64},{"hostname": "web-server-s1", "cpu": 128, "ram": 256}]

json_response = data.to_json

server = WEBrick::HTTPServer.new(Port: PORT)

server.mount_proc '/' do |req, res|
	res.status = 200
	res['Content-Type'] = 'application/json'
	res.body = json_response
end

trap('INT') { server.shutdown }

server.start

