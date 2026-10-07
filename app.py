from flask import Flask, request
from models import db
from tickets.routes import tickets_bp
from auth.routes import auth_bp
from config import Config
# db.init_app(app)
# with app.app_context():
#     db.create_all()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(auth_bp)

    return app