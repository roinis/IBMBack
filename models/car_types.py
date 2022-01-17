from constants import db as db_consts
from models.crud import Crud
from db_utils import db

class CarTypes(Crud):
    __tablename__ = 'car_types'
    id = (db_consts.INT_TYPE,'pk')
    name = (db_consts.STRING_TYPE,)


    @classmethod
    def get_table_attributes(cls):
        attributes = ['id', 'name']
        return {attribute: getattr(cls, attribute) for attribute in attributes}

    @classmethod
    def insert_init_values(cls):
        return[(['name'],['Honda']),
               (['name'],['Mazda'])]

    @classmethod
    def get_car_type_by_id(cls, id):
        connection = db.connection
        cursor = connection.cursor()
        car_type_query = cls.read(filters=['id'])
        car_type = cursor.execute(car_type_query,{"id": id}).fetchall()
        connection.commit()
        return car_type


