import utils
import fastems
import requests
from lxml import objectify
from datetime import datetime, timedelta


mms_base_uri = 'http://fpc27536s1/MMS5/'
order_times_format = '%Y-%m-%dT%H:%M:%SZ'


def build_request_params(service, soap_action, data):
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


def parse_response(response):
    root = objectify.fromstring(response.text)

    return utils.xml_to_dict(root)['Body']


def get_all_process_plans():
    data = '<GetItemBaseData xmlns="http://Fastems.Ui"></GetItemBaseData>'

    soap_request = build_request_params('BaseDataService', 'Fastems.Ui/IBaseDataService/GetItemBaseData', data)

    response = requests.post(**soap_request)

    plans = fastems.parse_response(response)

    return plans['GetItemBaseDataResponse']['GetItemBaseDataResult']['Data']


def create_order(order_data):
    payload = utils.format_template('./templates/CreateOrder.xml', order_data)

    request_params = {
        'data': payload,
        'service': 'OrderService',
        'soap_action': 'Fastems.Ui/IOrderService/CreateOrder'
    }

    soap_request = build_request_params(**request_params)

    return requests.post(**soap_request)


if __name__ == '__main__':
    order_data = {
        'gid': 'a0f77636-8ca6-4893-8aa4-a6be006a14b7',
        'part_number': '8029-3-296',
        'description': 'Batch gid Test',
        'order_number': 12345,
        'quantity': 1000000,
        'status': 'Planned',
        'start_date': datetime.now().strftime(order_times_format),
        'due_date': (datetime.now() + timedelta(days=5)).strftime(order_times_format)
    }

    response = fastems.create_order(order_data)

    print(response.text)
