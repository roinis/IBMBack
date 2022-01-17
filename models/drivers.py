from constants import db as db_consts
from models.crud import Crud
from db_utils import db


class Drivers(Crud):
    __tablename__ = 'drivers'
    id = (db_consts.INT_TYPE,'pk')
    name = (db_consts.STRING_TYPE,)

    @classmethod
    def get_table_attributes(cls):
        attributes = ['id', 'name']
        return {attribute: getattr(cls, attribute) for attribute in attributes}


    @classmethod
    def insert_init_values(cls):
        return[(['name'],['Hamilton']),
               (['name'],['Verstappen'])]

    @classmethod
    def get_driver_by_id(cls, id):
        connection = db.connection
        cursor = connection.cursor()
        driver_query = cls.read(filters=['id'])
        driver = cursor.execute(driver_query,{"id": id}).fetchall()
        connection.commit()
        return driver