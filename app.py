from flask import Flask
from resources.status_order import status_order_bp
from resources.orders import order_bp
from resources.weather import weather_bp
from database.commons import setup
import os
app = Flask(__name__)
setup.create_tables()

app.register_blueprint(status_order_bp)
app.register_blueprint(order_bp)
app.register_blueprint(weather_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.getenv('PORT'))  