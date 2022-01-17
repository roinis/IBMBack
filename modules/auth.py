import jwt
from constants import app
from modules.exceptions import AuthException
from http.cookies import SimpleCookie
from constants import app
from functools import wraps



def login_required(f):
    @wraps(f)
    def decorated(request_params):
        cookies_raw = request_params.get('HTTP_COOKIE')
        cookies = SimpleCookie()
        cookies.load(cookies_raw)
        if 'user_token' not in cookies:
            raise AuthException()
        try:
            token_data = jwt.decode(cookies.get('user_token').value, app.SECRET_KEY)
        except jwt.ExpiredSignatureError as e:
            raise AuthException()
        except Exception as e :
            raise Exception()
        return f(request_params)
    return decorated





