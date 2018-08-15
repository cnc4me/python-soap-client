import logging

from flask import Flask, jsonify

import schedule
from fastems.services import bp as services_routes

app = Flask(__name__)

app.config.from_pyfile('config.py')

handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
handler.setLevel(app.config['LOGGING_LEVEL'])
handler.setFormatter(logging.Formatter(app.config['LOGGING_FORMAT']))

app.logger.addHandler(handler)
app.register_blueprint(services_routes)


@app.errorhandler(500)
@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return str(e)
    # return render_template('500.htm'), 500


@app.route('/')
def index():
    return jsonify({'msg': "Welcome to the Fastems Bridge"})


@app.route('/schedule')
def get_orders_payload():
    return jsonify(schedule.get_scheduled_work())
