from constants import db as db_consts
from models.crud import Crud
from db_utils import db

class Reports(Crud):
    __tablename__ = "reports"
    id = (db_consts.INT_TYPE, 'pk')
    car_id = (db_consts.INT_TYPE, 'fk', 'cars', 'id')
    accident = (db_consts.INT_TYPE,)
    braking = (db_consts.FLOAT_TYPE,)
    accelerating = (db_consts.FLOAT_TYPE,)
    X = (db_consts.INT_TYPE,)
    Y = (db_consts.INT_TYPE,)
    datetime = (db_consts.STRING_TYPE,)

    @classmethod
    def get_table_attributes(cls):
        attributes = ['id', 'car_id', 'accident', 'braking', 'accelerating', 'X', 'Y', 'datetime']
        return {attribute: getattr(cls, attribute) for attribute in attributes}

    @classmethod
    def create_report(cls,object_data):
        columns, values = list(object_data.keys()), list(object_data.values())
        connection = db.connection
        cursor = connection.cursor()
        insert_query = cls.create_query(columns)
        cursor.execute(insert_query, values)
        connection.commit()

    @classmethod
    def get_all_reports(cls):
        connection = db.connection
        cursor = connection.cursor()
        report_query = cls.read(filters=[])
        reports = cursor.execute(report_query).fetchall()
        connection.commit()
        return reports




if __name__ == "__main__":
    print(Reports.create_table_query())
    # for property, value in vars(Reports):
    #     print(property, ":", value)
