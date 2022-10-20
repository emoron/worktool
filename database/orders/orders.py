import  sqlite3
from sqlite3 import Error
from ..commons.connection import create_connection

path_db = "database/orders.db"

def insert_value(data):
    
    conn = create_connection(path_db)
    
    sql = """ INSERT INTO orders (ord_id, ord_dt, qt_ordd)
             VALUES(?, ?, ?)
    """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    
    except Error as error:
        print('Error at function insert orders: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()

def select_by_id(_id):
    conn = create_connection(path_db)
    sql = '''SELECT * FROM orders WHERE id = {}'''.format(_id)
    
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
    sql = 'SELECT * FROM orders'
    
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        data = [dict(row) for row in rows]
        resp_dict = []
        for order in data:
            date = order['ord_dt'].split('/',1)[1] #2019/12/05
            if date >= '03/19' or date <= '06/19':
                resp = {'ord_id': order['ord_id'], 'season': 'Spring'}
            if date >= '06/20' or date <= '09/21':
                resp = {'ord_id': order['ord_id'], 'season': 'Summer'}
            if date >= '09/22' or date <= '12/20':
                resp = {'ord_id': order['ord_id'], 'season': 'Fall'}
            if date >= '12/21' or date <= '03/18':
                resp = {'ord_id': order['ord_id'], 'season': 'Winter'}
            resp_dict.append(resp)
        print(resp_dict)
        return resp_dict 
    
    except Error as error:
        print('Error at function select all orders: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()
            
