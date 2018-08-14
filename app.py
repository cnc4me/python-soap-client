import logging
from datetime import date, datetime, timedelta

from flask import Flask, jsonify
from flask.json import JSONEncoder

import config
import fastems
import fastemsdate
import schedule
from services import bp as services_routes


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return fastemsdate.to_string(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

app.config.from_object(config)
# app.config.from_envvar('FASTEMS_BRIDGE_SETTINGS')

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


@app.route('/scheduled-work')
def get_orders_payload():
    return jsonify(schedule.get_scheduled_work())


@app.route('/gids')
def get_all_gids():
    return jsonify({plan['Name']: plan['Id'] for plan in fastems.get_base_data()})


