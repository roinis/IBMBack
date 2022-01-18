import json
from wsgiref import simple_server, util
from modules.exceptions import *


#routing
from routes.auth import Auth
from routes.report import Report
from routes.car import Car
from routes.car_type import CarType
from routes.driver import Driver
from routes.suspicious import Suspicious
from routes.index import Index


class WebServer:
    routing_table = {
        'auth': Auth,
        'report': Report,
        'car_type': CarType,
        'car': Car,
        'driver': Driver,
        'suspicious': Suspicious,
        'index': Index
    }

    def app(self, environ, start_response):
        headers = [('Content-type', 'application/json; charset=utf-8'),('Access-Control-Allow-Origin','http://127.0.0.1:5500')
                   ,('Access-Control-Allow-Credentials','true')]
        status = '200 OK'
        return_val = {}
        base_route = environ.get('PATH_INFO').split('/')[1]
        try:
            if base_route == '' or base_route == 'favicon.ico':
                return_val = {}
            elif base_route in WebServer.routing_table:
                return_val = WebServer.routing_table[base_route].handle_request(environ)
                if 'auth' in environ.get('PATH_INFO'):
                    headers.append(('Set-Cookie',f'user_token={return_val};max-age=600;SameSite=Strict;Path=/'))
                    return_val = {}
            else:
                raise ResourceNotFound()
        except AuthException as e:
            status = '403 '
        except ResourceNotFound as e:
            status = '404 '
        except Exception as e:
            print(e)
            status = '500 '
        start_response(status, headers)
        return_val = json.dumps(return_val).encode('utf-8')
        return [return_val]


    def start_web_server(self):
        httpd = simple_server.make_server('', 8000, self.app)
        try:
            print('Start Web Server')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down.")
            httpd.server_close()



if __name__ == '__main__':
    web_server = WebServer()
    web_server.start_web_server()