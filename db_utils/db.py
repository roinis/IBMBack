import sqlite3
from constants import db as db_consts

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect(db_consts.DB_PATH)
connection.row_factory = dict_factory

