import os
from modules.auth import login_required
from models.cars import Cars
from modules.exceptions import *

POSSIBLE_METHODS = ['get']


class Car:
    @staticmethod
    @login_required
    def handle_request(request_params):
        request_method = request_params.get('REQUEST_METHOD').lower()
        if request_method not in POSSIBLE_METHODS:
            raise ResourceNotFound()
        return getattr(Car, request_method)(request_params)

    @staticmethod
    def get(request_params):
        path = request_params.get('PATH_INFO', '')
        if not path:
            raise ResourceNotFound()
        id = os.path.basename(path)
        try:
            id = int(id)
        except ValueError as e:
            raise ResourceNotFound()
        return Cars.get_car_by_id(id)
