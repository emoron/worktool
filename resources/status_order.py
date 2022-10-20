from flask import request, jsonify, Blueprint
from database.order_status import tasks


status_order_bp = Blueprint('routes-status', __name__)

@status_order_bp.route('/tasks', methods=['POST'])
def add_task():
    order_number = request.json['order_number']
    item_name = request.json['item_name']
    status_order = request.json['status_order']
    
    data = (order_number, item_name, status_order)
    task_id = tasks.insert_task(data)
    
    if task_id:
        by_order_number = tasks.select_task_by_order_number(task_id)
        return jsonify({'task': by_order_number})
    
    return jsonify({'messages': 'Internal Error'})

@status_order_bp.route('/tasks', methods=['GET'])
def get_tasks():
    data = tasks.select_all_task()
    if data:
        return jsonify({'tasks': data})
    elif data == False:
        return jsonify({'messages': 'Internal Error'})
    else:
        return jsonify({'tasks': {}})
    
@status_order_bp.route('/tasks', methods=['PUT'])
def update_task():
    status_order = request.json['status_order']
    id_arg = request.args.get('id')
    
    if tasks.update_tasks(id_arg, (status_order,)):
        task = tasks.select_task_by_order_number(id_arg)
        return jsonify(task)
    return jsonify({'message': 'Internal Error'})

@status_order_bp.route('/order_status', methods=['GET'])
def get_tasks_for_order_number():
    
    task = tasks.select_task_for_order_number()
    
    if tasks:
        return jsonify({'customer': task})
    return jsonify({'message': 'Internal Error'})