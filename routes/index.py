from constants import app

POSSIBLE_METHODS = ['get']

class Index:
    @staticmethod
    def handle_request(request_params):
        request_method = request_params.get('REQUEST_METHOD').lower()
        if request_method not in POSSIBLE_METHODS:
            raise Exception('No method')
        return getattr(Index,request_method)(request_params)

    @staticmethod
    def get(request_params):
        with open(f'{app.UI_DIR}/index.html', 'rb') as f:
            return f.read()