#! /usr/bin/env python

### Since there's a pi zero for the camera/vision and a pi for the robot (and they must communicate) :
### Use the AIY vision kit to set up wifi, then share wifi through ethernet between pi zero and the pi running the robot.
### https://raspberrypi.stackexchange.com/questions/48307/sharing-the-pis-wifi-connection-through-the-ethernet-port

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import json
from Looker import Looker
import SocketServer

config = json.loads(open('config.json').read())
looker = Looker()

class RequestHandler(BaseHTTPRequestHandler) :

  def _set_headers(self) :
    self.send_response(200, 'OK')
    self.send_header('Content-type', 'application/json')
    self.end_headers()

  def send_person_response(self) :
    result = looker.identify_it('person')
    return json.dumps({'success': result.success, 'answer': result.answer, 'what': result.obj_type})

  def send_object_response(self) :
    result = looker.identify_it('object')
    return json.dumps({'success': result.success, 'answer': result.answer, 'what': result.obj_type})

  def do_GET(self) :
    referer = self.headers.get('Referer')
    if referer is None :
      referer = '/'
    msg = json.dumps({'message': 'WASSSUP!?!?!?!?!?'})
    referer = referer.split('/')
    self._set_headers()
    if referer[-2] == 'identify' :
      if referer[-1] == 'person' :
        msg = self.send_person_response()
      elif referer[-1] == 'object' :
        msg = self.send_object_response()
    self.wfile.write(msg)

def run() :
  HOST = config['http_host']
  PORT = config['http_port']
  httpd = HTTPServer((HOST, PORT), RequestHandler)
  print("serving at port", PORT)
  httpd.serve_forever()

if __name__ == '__main__' :
  run()
