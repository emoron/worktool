import  sqlite3
from sqlite3 import Error
from ..commons.connection import create_connection


path_db = "database/tasks.db"
def insert_task(data):
    
    conn = create_connection(path_db)
    
    sql = """ INSERT INTO tasks (order_number, item_name, status_order)
             VALUES(?, ?, ?)
    """
    
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid
    
    except Error as error:
        print('Error at function insert task: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()


def select_task_by_order_number(_id):
    conn = create_connection(path_db)
    sql = f'SELECT * FROM tasks WHERE id = {_id}'
    
    try:
        conn.row_factory = sqlite3.Row
        cur= conn.cursor()
        cur.execute(sql)
        by_order_number = dict(cur.fetchone())
        return by_order_number
        
    except Error as error:
        print('Error at select order number: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()
            
def select_all_task():
    conn = create_connection(path_db)
    sql = 'SELECT * FROM tasks '
    
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        task_rows = cur.fetchall()
        tasks = [dict(row) for row in task_rows]
        return tasks
    
    except Error as error:
        print('Error at function select all tasks: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()
            
def select_task_for_order_number():
    conn = create_connection(path_db)
    sql = ''' SELECT * FROM tasks '''
    
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql)
        task_rows = cur.fetchall()
        tasks = [dict(row)for row in task_rows]
        order_number_unique = list(set([task['order_number'] for task in tasks]))
        resp = [] 
          
        for i in order_number_unique:
            status_all = []
            status_value = 'CANCELLED'
            for j in tasks:
                if i == j['order_number'] and j['status_order'] != 'CANCELLED':
                    status_all.append(j['status_order'])
                status = list(set(status_all))
                
                len_status = len(status)
                    
                if len_status == 1:
                    status_value = status[0]
                elif len_status > 1:
                    status_value = 'PENDING'
             
            resp.append({'order_number': i, 'status_order': status_value})

        return resp
    
    except Error as error:
        print('Error at function select all tasks: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()


def update_tasks(_id, data):
    conn = create_connection(path_db)
    sql = ''' UPDATE tasks SET status_order = ? 
                WHERE id = {}'''.format(_id)
                
    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    
    except Error as error:
        print('Error at function update tasks: {}'.format(error))
        return False
    
    finally:
        if conn:
            cur.close()
            conn.close()