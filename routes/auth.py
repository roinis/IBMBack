import json,jwt
from hashlib import sha256
from datetime import datetime, timedelta
from modules.exceptions import AuthException
from models.users import Users
from constants import app

POSSIBLE_METHODS = ['post','options']

class Auth:
    @staticmethod
    def handle_request(request_params):
        request_method = request_params.get('REQUEST_METHOD').lower()
        if request_method not in POSSIBLE_METHODS:
            raise Exception('No method')
        return getattr(Auth,request_method)(request_params)

    @staticmethod
    def post(request_params):
        try:
            request_body_size = int(request_params.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0
        request_body = request_params['wsgi.input'].read(request_body_size)
        data = json.loads(request_body)
        username, password = data.get('username'), data.get('password')
        if not username or not password:
            raise AuthException()
        hash_password = sha256(password.encode('utf-8')).hexdigest()
        user = Users.get_user_by_name(username)
        if not user or user.get('password') != hash_password:
            raise AuthException()
        token = jwt.encode({'user':username, 'exp':datetime.utcnow() + timedelta(hours=4)}, app.SECRET_KEY)
        print(token.decode('utf-8'))
        return token.decode('utf-8')

    @staticmethod
    def options(request_params):
        return True
