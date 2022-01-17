from os import path

CURR_DIR = path.dirname(__file__)
ASSETS_DIR = path.join(path.dirname(CURR_DIR), 'assets')


DB_NAME = "pinpoint.db"
DB_PATH = path.join(ASSETS_DIR, DB_NAME)

INT_TYPE = "INTEGER"
NULL_TYPE = "NULL"
FLOAT_TYPE = "REAL"
STRING_TYPE = "TEXT"
BLOB_TYPE = "BLOB"

PRIMARY_KEY = "PRIMARY KEY"
FOREIGN_KEY = "FOREIGN KEY ({}) REFERENCES {} ({})"

SELECT_ALL = "SELECT * FROM {}"