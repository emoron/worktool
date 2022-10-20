import sqlite3
from sqlite3 import Error
from .connection import create_connection


def read_file(path):
    with open(path, 'r') as sql_file:
        return sql_file.read()

def create_tables():
    conn = create_connection("database/weather.db")
    path = 'database/sql/tables.sql'
    
    sql = read_file(path)
    
    try:
        cur = conn.cursor()
        cur.executescript(sql)
        conn.commit()
        return True
    
    except Error as error:
        print('Error at create tables: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()