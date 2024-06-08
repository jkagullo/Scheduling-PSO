from flask import Flask
from .blueprints.home import home
from .blueprints.form import form
from .blueprints.schedule import schedule

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(form)
    app.register_blueprint(schedule)
    
    return app