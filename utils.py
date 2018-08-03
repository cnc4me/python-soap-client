import re
import json


def load_xml_template(filename):
    with open(filename, 'r') as xml_file:
        return re.sub(r'\>\s+\<', '><', xml_file.read().replace('\n', ''))


def format_template(filename, data):
   return load_xml_template(filename).format(**data)


def pretty_print_json(obj):
    print(json.dumps(obj, indent=2, sort_keys=True))


def stuff_envelope(xml_str):
    return '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"><s:Body>%s</s:Body></s:Envelope>' % xml_str


def xml_to_dict(element):
    arrayables = {
        'Data',
        'Steps',
        'Programs',
        'Operations',
        'MaterialOperations',
        'AlternativeProcessPlans',
    }

    if re.sub(r'{.*}', '', element.tag) in arrayables:
        return [xml_to_dict(e) for e in element.getchildren()]
    else:
        if element.getchildren():
            return {re.sub(r'{.*}', '', e.tag): xml_to_dict(e) for e in element.getchildren()}
        else:
            return str(element.pyval)


if __name__ == '__main__':
    print(load_xml_template('./templates/CreateOrder.xml'))