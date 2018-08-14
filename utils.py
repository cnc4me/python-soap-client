import re
from datetime import datetime

import jsonpickle
from lxml import objectify
from requests import Response

import fastemsdate


class DatetimeHandler(jsonpickle.handlers.BaseHandler):
    def flatten(self, obj, data):
        if isinstance(obj, datetime):
            return fastemsdate.to_string(obj)


jsonpickle.handlers.registry.register(datetime, DatetimeHandler)


def load_xml_template(filename):
    with open(filename, 'r') as xml_file:
        return re.sub(r'\>\s+\<', '><', xml_file.read().replace('\n', ''))


def format_template(filename, data):
    return load_xml_template(filename).format(**data)


def print_json(obj):
    print(jsonpickle.dumps(obj, unpicklable=False))


def stuff_envelope(xml_str):
    return '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body>%s</s:Body></s:Envelope>' % xml_str


def parse_response(response: Response):
    root = objectify.fromstring(response.text)

    return xml_to_dict(root)['Body']


def xml_to_dict(element):
    arrayables = (
        'Data',
        'Steps',
        'Programs',
        'Operations',
        'MaterialOperations',
        'AlternativeProcessPlans',
    )

    if re.sub(r'{.*}', '', element.tag) in arrayables:
        return [xml_to_dict(e) for e in element.getchildren()]
    else:
        if element.getchildren():
            return {re.sub(r'{.*}', '', e.tag): xml_to_dict(e) for e in element.getchildren()}
        else:
            return str(element)
