from datetime import datetime
from random import randint

import requests

import fastemsdate
import utils
from services import Services

mms_base_uri = 'http://fpc27536s1/MMS5/'


def get_base_data():
    response = Services.BaseData.service.GetItemBaseData()

    return response['Data']['ItemBaseDataDto']


def get_part_number_to_gid_dict():
    return {i['Name']: i['Id'] for i in get_base_data()}


def create_order(order_data):
    payload = utils.format_template('./templates/CreateOrder.xml', order_data)

    request_params = {
        'data': payload,
        'service': 'OrderService',
        'soap_action': 'Fastems.Ui/IOrderService/CreateOrder'
    }

    soap_request = _build_request_params(**request_params)

    return requests.post(**soap_request)


def _build_request_params(service, soap_action, data):
    return {
        'url': mms_base_uri + 'Services/' + service + '.svc',
        'data': utils.stuff_envelope(data),
        'headers': {
            'Accept': '*/*',
            'Referer': mms_base_uri + 'DataManager.xap?ignore={:%m-%d-%Y %H:%M:%S %p}'.format(datetime.now()),
            'Accept-Language': 'en-US',
            'Content-Length': str(len(data)),
            'Content-Type': 'text/xml; charset=utf-8',
            'SOAPAction': 'http://' + soap_action,
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; McAfee; InfoPath.2)',
            'Host': 'fpc27536s1',
            'DNT': '1',
            'Connection': 'Keep-Alive',
            'Cache-Control': 'no-cache'
        }
    }


if __name__ == '__main__':
    order_data = {
        'gid': 'a0f77636-8ca6-4893-8aa4-a6be006a14b7',
        'part_number': '8029-3-296',
        'description': 'Batch Order Creation Test',
        'order_number': 99999,
        'quantity': randint(10000, 90000),
        'status': 'Planned',
        'start_date': fastemsdate.start_now(),
        'due_date': fastemsdate.days_from_now(5)
    }

    response = create_order(order_data)
    result = utils.parse_response(response)['CreateOrderResponse']

    print(result)
