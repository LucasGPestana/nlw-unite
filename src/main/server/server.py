from flask import Flask
from flask_cors import CORS

from src.models.settings.connection import DB_CONNECTION_HANDLER

from src.main.routes.event_routes import event_route_bp
from src.main.routes.attendees_routes import attendees_route_bp
from src.main.routes.check_ins_routes import check_ins_route_bp

DB_CONNECTION_HANDLER.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)
app.register_blueprint(attendees_route_bp)
app.register_blueprint(check_ins_route_bp)