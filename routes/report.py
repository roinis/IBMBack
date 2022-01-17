import json, pandas as pd
import math

from modules.auth import login_required
from datetime import datetime
from models.reports import Reports
from modules.exceptions import *

POSSIBLE_METHODS = ['post', 'get']


class Report:
    @staticmethod
    @login_required
    def handle_request(request_params):
        request_method = request_params.get('REQUEST_METHOD').lower()
        if request_method not in POSSIBLE_METHODS:
            raise Exception('No method')
        return getattr(Report, request_method)(request_params)

    @staticmethod
    def create_new_report(json_data):
        object_data = dict(car_id=json_data.get('car_id'), accident=json_data.get('accident'),
                           braking=json_data.get('braking'), accelerating=json_data.get('accelerating'),
                           X=json_data.get('X'), Y=json_data.get('Y'), datetime=datetime.now().isoformat())
        Reports.create_report(object_data)
        return object_data

    @staticmethod
    def get_latest_accidents_vector(area_km, history_accidents_limit):
        square_area_km = math.floor(math.sqrt(area_km))
        reports = pd.DataFrame(Reports.get_all_reports())
        reports['datetime'] = pd.to_datetime(reports['datetime'], format='%Y-%m-%dT%H:%M:%S.%f')
        reports = reports.sort_values(by="datetime", ascending=False)
        reports = reports[reports['accident'] == 1]
        reports = reports.head(history_accidents_limit)
        reports = reports[(reports['X'] <= square_area_km) & (reports['Y'] <= square_area_km)]

        number_of_accidents = reports.shape[0]
        max_square_coordinate = int(max([reports['X'].max(), reports['Y'].max()], default=0))

        return dict(number_of_accidents=number_of_accidents, X=max_square_coordinate, Y=max_square_coordinate)

    @staticmethod
    def post(request_params):
        print(request_params)
        try:
            request_body_size = int(request_params.get('CONTENT_LENGTH', 0))
        except ValueError:
            request_body_size = 0

        request_body = request_params['wsgi.input'].read(request_body_size)
        data = json.loads(request_body)
        if request_params.get('PATH_INFO', '') == '/report':
            return Report.create_new_report(data)
        elif request_params.get('PATH_INFO', '') == '/report/latest_accidents_vector':
            return Report.get_latest_accidents_vector(data.get('area_km', 0), data.get('history_accidents_limit', 0))
        raise ResourceNotFound()

    @staticmethod
    def get(request_params):
        print(request_params)
        return Reports.get_all_reports()
