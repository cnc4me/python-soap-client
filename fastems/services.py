import io
import operator

from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport

import config
from fastems.plugins import FastemsHeadersPlugin


def _get_client(service):
    session = Session()
    session.auth = HTTPBasicAuth('mmsuser', 'user')

    transport = Transport(cache=SqliteCache(), session=session)
    wsd_uri = 'http://%s/MMS5/Services/%sService.svc?wsdl' % (config.FASTEMS_HOST, service)

    return Client(wsd_uri, transport=transport, plugins=[FastemsHeadersPlugin()])


class Services(object):
    User = _get_client('User')
    Tool = _get_client('Tool')
    Cell = _get_client('Cell')
    Query = _get_client('Query')
    Order = _get_client('Order')
    System = _get_client('System')
    Device = _get_client('Device')
    Pallet = _get_client('Pallet')
    BaseData = _get_client('BaseData')
    Workplace = _get_client('Workplace')
    ControlRoom = _get_client('ControlRoom')
    FactoryCalendar = _get_client('FactoryCalendar')

    @staticmethod
    def dump(service):
        string = io.StringIO()

        wsdl = getattr(Services, service).wsdl

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
