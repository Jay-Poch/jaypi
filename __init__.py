from flask import Flask, Blueprint
from routes.terminal import terminal_blueprint
from routes.hobby import hobby_blueprint
from routes.random_message import random_message # type: ignore
def create_app():
    app = Flask(__name__)
    app.register_blueprint(terminal_blueprint)
    app.register_blueprint(hobby_blueprint)
    app.register_blueprint(random_message)
    return app
 
