from constants import db as db_consts
from models.crud import Crud
from db_utils import db


class Cars(Crud):
    __tablename__ = 'cars'
    id = (db_consts.INT_TYPE,'pk')
    car_type_id = (db_consts.INT_TYPE,'fk','car_types','id')
    driver_id = (db_consts.INT_TYPE, 'fk', 'drivers','id')

    @classmethod
    def get_table_attributes(cls):
        attributes = ['id', 'car_type_id', 'driver_id']
        return {attribute: getattr(cls, attribute) for attribute in attributes}


    @classmethod
    def insert_init_values(cls):
        return[(['car_type_id','driver_id'],[1,1]),
               (['car_type_id','driver_id'],[2,2])]
    @classmethod
    def get_car_by_id(cls, id):
        connection = db.connection
        cursor = connection.cursor()
        car_query = cls.read(filters=['id'])
        car = cursor.execute(car_query,{"id": id}).fetchall()
        connection.commit()
        return car