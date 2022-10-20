from flask import request, jsonify, Blueprint
from database.orders import orders
from datetime import datetime


order_bp = Blueprint('routes-orders', __name__)

@order_bp.route('/orders', methods=['POST'])
def add_order():
    ord_id = request.json['ord_id']
    ord_dt = request.json['ord_dt']
    qt_ordd = request.json['qt_ordd']
    
    data = (ord_id, ord_dt, qt_ordd)
    order_id = orders.insert_value(data)
    
    if order_id:
        by_order_id = orders.select_by_id(order_id)
        return jsonify({'orders': by_order_id})
    
    return jsonify({'messages': 'Internal Error'})

@order_bp.route('/orders', methods=['GET'])
def get_orders():
    data = orders.select_all()
    if data:
        return jsonify({'orders': data})
    elif data == False:
        return jsonify({'messages': 'Internal Error'})
    else:
        return jsonify({'message': {}})
