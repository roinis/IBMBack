from constants import db as db_consts
from models.crud import Crud
from db_utils import db

class Users(Crud):
    __tablename__ = 'users'
    id = (db_consts.INT_TYPE,'pk')
    user = (db_consts.STRING_TYPE,)
    password = (db_consts.STRING_TYPE,)
    mail = (db_consts.STRING_TYPE,)

    @classmethod
    def get_table_attributes(cls):
        attributes = ['id', 'user', 'password', 'mail']
        return {attribute: getattr(cls, attribute) for attribute in attributes}


    @classmethod
    def insert_init_values(cls):
        return[
            (['user','password','mail'],['gadi','8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92','gadi@walla.com']),#123456
               (['user','password','mail'],['aviv','e54fc6b51915e222ba6196747a19ebb8dfa651fd2b46a385a0ded647fbfefda0','aviv@walla.com']) #789456
               ]

    @classmethod
    def get_user_by_name(cls, username):
        connection = db.connection
        cursor = connection.cursor()
        query = cls.read(['user'])
        user = cursor.execute(query,{'user':f"{username}"}).fetchall()
        if not user:
            return None
        return user[0]
