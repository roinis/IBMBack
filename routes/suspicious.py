import json
from constants import app
from datetime import datetime
from models.reports import Reports

POSSIBLE_METHODS = ['post']

class Suspicious:
    @staticmethod
    def handle_request(request_params):
        request_method = request_params.get('REQUEST_METHOD').lower()
        if request_method not in POSSIBLE_METHODS:
            raise Exception('No method')
        return getattr(Suspicious,request_method)(request_params)

    @staticmethod
    def post(request_params):
        try:
            request_body_size = int(request_params.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0

        request_body = request_params['wsgi.input'].read(request_body_size)
        data = json.loads(request_body)
        log_data = data.get('data', '')
        with open(app.LOGGER_PATH,'a') as f:
            f.write(log_data + "\n")