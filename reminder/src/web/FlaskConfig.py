import os

from flask import Flask
from flask_cors import CORS

from src.controller.ReminderController import reminder_controller
from src.controller.WatchedController import watched_controller


class FlaskConfig:
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    def __call__(self):
        self.register_blue_prints()
        self.run_app()

    def register_blue_prints(self):
        self.app.register_blueprint(reminder_controller)
        self.app.register_blueprint(watched_controller)

    def run_app(self):
        self.app.run(
            debug=True,
            use_reloader=False,
            host=os.getenv("FLASK_HOST"),
            port=os.getenv("FLASK_PORT")
        )
