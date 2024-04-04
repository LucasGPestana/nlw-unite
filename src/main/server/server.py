from flask import Flask
from flask_cors import CORS

from src.models.settings.connection import DB_CONNECTION_HANDLER
from src.main.routes.event_routes import event_route_bp

DB_CONNECTION_HANDLER.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)