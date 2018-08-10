import logging
from datetime import datetime, timedelta

from flask import Flask, jsonify

import fastems
import fastemsdate
import schedule
from fastemsdate import FASTEMS_ORDER_FORMAT
from services import Services
from flask.json import JSONEncoder
from datetime import date


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

app.config.from_object('config')
# app.config.from_envvar('FASTEMS_BRIDGE_SETTINGS')

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


@app.route("/")
def index():
    return jsonify({'msg':"Welcome to the Fastems Bridge"})


@app.route('/csv')
def parse_schedule():
    return jsonify(schedule.get_scheduled_work())


@app.route('/scheduled-work')
def get_orders_payload():
    gid_map = fastems.get_part_number_to_gid_dict()
    scheduled_work = schedule.get_scheduled_work()

    orders_payload = []

    for job in scheduled_work:
        if job['part_number'] in gid_map:
            job['gid'] = gid_map[job['part_number']]
            orders_payload.append(job)

    return jsonify(orders_payload)


@app.route('/gids')
def get_all_gids():
    plans = fastems.get_all_process_plans()

    return jsonify({plan['Name']: plan['Id'] for plan in plans})


@app.route('/zeep')
def get_process_plans():
    response = Services.BaseData.service.GetItemBaseData()

    base_data = response['Data']['ItemBaseDataDto']

    return jsonify([{
        'part_number': data_item['Name'],
        'gid': data_item['Id']
    } for data_item in base_data])


@app.route('/process-plans')
def get_all_process_plans():
    return jsonify(fastems.get_all_process_plans())


@app.route('/test/create-order')
def create_order():
    order_data = {
        'gid': 'a0f77636-8ca6-4893-8aa4-a6be006a14b7',
        'part_number': '8029-3-296',
        'description': 'Batch gid Test',
        'order_number': 12345,
        'quantity': 1000000,
        'status': 'Planned',
        'start_date': datetime.now().strftime(FASTEMS_ORDER_FORMAT),
        'due_date': (datetime.now() + timedelta(days=5)).strftime(FASTEMS_ORDER_FORMAT)
    }

    r = fastems.create_order(order_data)

    print(r.text)
