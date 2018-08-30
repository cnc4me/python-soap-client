import logging

from flask import Flask, jsonify, render_template

import fastems
import schedule

app = Flask(__name__)

app.config.from_pyfile('config.py')

handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
handler.setLevel(app.config['LOGGING_LEVEL'])
handler.setFormatter(logging.Formatter(app.config['LOGGING_FORMAT']))

app.logger.addHandler(handler)


@app.errorhandler(500)
@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error('Unhandled Exception: %s', (e))
    return str(e)
    # return render_template('500.htm'), 500


@app.route('/')
def index():
    return jsonify({'msg': "Welcome to the Fastems Bridge"})


@app.route('/gids')
def get_gids():
    return jsonify(fastems.get_part_number_to_gid_dict())


@app.route('/schedule')
def get_orders_payload():
    s = schedule.Schedule(app.config['SCHEDULE_CSV_PATH'])

    return jsonify(s.get_all())


@app.route('/services')
def service_list():
    services = fastems.services.__all__
    services.sort()
    return render_template('services.html', services=services)


@app.route('/services/<service>')
def service(service):
    return render_template('wsdl.html', service=service, wsdl=Services.dump(service))


@app.route('/operations/<service>')
def operations(service):
    return render_template('wsdl.html', service=service, wsdl=Services.operations(service))
