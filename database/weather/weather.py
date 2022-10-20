import  sqlite3
from sqlite3 import Error
from ..commons.connection import create_connection

path_db = "database/weather.db"

def insert_value(data):
    
    conn = create_connection(path_db)
    
    sql = """ INSERT INTO weather (date_of_rainy, was_rainy)
             VALUES(?, ?)
    """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    
    except Error as error:
        print('Error at function insert weather: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def select_by_id(_id):
    conn = create_connection(path_db)
    sql = '''SELECT * FROM weather WHERE id = {}'''.format(_id)
    
    try: 
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        by_id = dict(cur.fetchone())
        return by_id
    
    except Error as error:
        print('Error at select order: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()
    
        
def select_all():
    conn = create_connection(path_db)
    sql = 'SELECT * FROM weather'
    
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        data = [dict(row) for row in rows]
        rain_dict = []
        temp = 0
        for rain in data:
            was_rain = rain['was_rainy']
            if was_rain == 'TRUE' and temp == 0:
                rain_dict.append({'date': rain['date_of_rainy'], 'was_rainy': rain['was_rainy']})
                temp = 1
            if was_rain == 'FALSE':
                temp = 0
        return rain_dict 
    
    except Error as error:
        print('Error at function select all weather: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()
            
