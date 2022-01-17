from constants import db as db_consts
from db_utils import db
from models.car_types import CarTypes
from models.drivers import Drivers
from models.cars import Cars
from models.reports import Reports
from models.users import Users


def init():
    connection = db.connection
    cursor = connection.cursor()

    # order does matter
    models = [CarTypes,Drivers,Cars,Reports,Users]
    for model in models:
        cursor.execute(model.create_table_query())
        if not "insert_init_values" in dir(model) or cursor.execute(db_consts.SELECT_ALL.format(model.__tablename__)).fetchall():continue

        insert_objects = model.insert_init_values()
        for columns,values in insert_objects:
            insert_query = model.create_query(columns)
            cursor.execute(insert_query,values)
        connection.commit()

