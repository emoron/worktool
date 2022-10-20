from flask import request, jsonify, Blueprint
from database.weather import weather


weather_bp = Blueprint('routes-weather', __name__)

@weather_bp.route('/weather', methods=['POST'])
def add_order():
    date_of_rainy = request.json['date_of_rainy']
    was_rainy = request.json['was_rainy']
    
    data = (date_of_rainy, was_rainy)
    weather_id = weather.insert_value(data)
    
    if weather_id:
        by_weather_id = weather.select_by_id(weather_id)
        return jsonify({'weather': by_weather_id})
    
    return jsonify({'messages': 'Internal Error'})

@weather_bp.route('/weather', methods=['GET'])
def get_orders():
    data = weather.select_all()
    if data:
        return jsonify({'weather': data})
    elif data == False:
        return jsonify({'messages': 'Internal Error'})
    else:
        return jsonify({'message': {}})
