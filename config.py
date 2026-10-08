import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE_PATH = os.path.join(BASE_DIR, "instance", "tickets.sqlite")

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "Juan3892098."

class TestConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_tickets.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "this-is-not-secret"
    TESTING = True