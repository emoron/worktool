import sqlite3
from sqlite3 import Error


def create_connection(path_db):
    conn = None
    
    try:
        conn = sqlite3.connect(path_db)
    
    except Error as error:
        print("Error connecting to database orders: {}".format(error))
    return conn