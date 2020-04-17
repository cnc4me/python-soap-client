import io
import operator
import re
import socket
from os import path

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.cache import SqliteCache
from zeep.plugins import HistoryPlugin
from zeep.transports import Transport

import config
from fastems.plugins import FastemsHeadersPlugin

__all__ = (
    'UserService',
    'ToolService',
    'CellService',
    'QueryService',
    'OrderService',
    'SystemService',
    'DeviceService',
    'PalletService',
    'BaseDataService',
    'FadectorService',
    'EstimatesService',
    'NcLibraryService',
    'WorkplaceService',
    'ControlRoomService',
    'RemoteAlarmService',
    'LocalizationService',
    'FactoryCalendarService',
    'ProductionSchedulerService')

Requestor = {
    'ApplicationName': 'DataManager',
    'HostName': socket.gethostname(),
    'UserName': config.DATA_MANAGER_USER,
}


class FastemsService(object):
    def __init__(self, service):
        self._requestor = Requestor
        self._client, self._history = build_client(service)

    def __str__(self):
        string = io.StringIO()
        wsdl = self._client.wsdl

        print("Prefixes:", file=string)
        for prefix, namespace in wsdl.types.prefix_map.items():
            print(' ' * 4, '%s: %s' % (prefix, namespace), file=string)

        print('', file=string)
        print("Bindings:", file=string)
        for binding_obj in sorted(wsdl.bindings.values(), key=lambda k: str(k)):
            print(' ' * 4, str(binding_obj), file=string)

        print('', file=string)
        for service in wsdl.services.values():
            print(str(service), file=string)
            for port in service.ports.values():
                print(' ' * 4, str(port), file=string)
                print(' ' * 8, 'Operations:', file=string)

                operations = sorted(
                    port.binding._operations.values(),
                    key=operator.attrgetter('name'))

                for operation in operations:
                    print('%s%s' % (' ' * 12, str(operation)), file=string)
                print('', file=string)

        print('', file=string)
        print("Global elements:", file=string)
        for elm_obj in sorted(wsdl.types.elements, key=lambda k: k.qname):
            value = elm_obj.signature(schema=wsdl.types)
            print(' ' * 4, value, file=string)

        print('', file=string)
        print("Global types:", file=string)
        for type_obj in sorted(wsdl.types.types, key=lambda k: k.qname or ''):
            value = type_obj.signature(schema=wsdl.types)
            print(' ' * 4, value, file=string)

        return string.getvalue()


def build_client(service) -> (Client, HistoryPlugin):
    '''Create a new Zeep client with history based on a service name'''
    history = HistoryPlugin()

    session = Session()
    session.auth = HTTPBasicAuth(config.DATA_MANAGER_USER, config.DATA_MANAGER_PASS)

    transport = Transport(cache=SqliteCache(), session=session)
    wsd_uri = 'http://%s/MMS5/Services/%s.svc?wsdl' % (config.FASTEMS_HOSTNAME, service)

    plugins = [FastemsHeadersPlugin(), history]

    return Client(wsd_uri, transport=transport, plugins=plugins), history


def _project_dir(file):
    return path.join(path.dirname(path.abspath(__file__)), file)


def generate_methods(service):
    methods = []

    print('Building %s Zeep Client' % service)
    client, history = build_client(service)

    for service in client.wsdl.services.values():
        for port in service.ports.values():
            operations = sorted(
                port.binding._operations.values(),
                key=operator.attrgetter('name'))

            for operation in operations:
                print(operation.__dict__)
                m = re.match(r'([a-zA-Z]+)\((.+)?\)', str(operation))

                if m:
                    param_def = ''
                    params = ''

                    if m.group(2):
                        param_def = m.group(2).split(', ')
                        params = ', '.join([p.split(': ')[0] for p in param_def])

                    methods.append({
                        'method_name': m.group(1),
                        'params': params,
                        'param_def': param_def
                    })
    return methods


def generate_class_files():
    class_template_file = './py_templates/class.tmpl'
    method_template_file = './py_templates/method.tmpl'

    for service in __all__:
        service_class_file = './%s.py' % service
        methods = generate_methods(service)
        # print(methods)

        print('Creating %s' % service_class_file)
        with open(class_template_file, 'r') as class_template, \
                open(method_template_file, 'r') as method_template, \
                open(service_class_file, 'w') as new_class:

            method_str = method_template.read()

            new_class.write(class_template.read().format(service_name=service))
            new_class.write('\n')

            for method in methods:
                print('[%s] Adding %s()' % (service, method['method_name']))
                new_class.write(method_str.format(**method))

            new_class.write('\n')

        print('Done!\n')


if __name__ == '__main__':
    generate_class_files()
