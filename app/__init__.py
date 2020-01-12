from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes
