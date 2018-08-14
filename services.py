import io
import operator
from datetime import datetime

from flask import Blueprint, render_template
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport

mms_base_uri = 'http://fpc27536s1/MMS5/'
bp = Blueprint('services', __name__, url_prefix='/services')


def _get_client(service):
    session = Session()
    session.auth = HTTPBasicAuth('mmsuser', 'user')
    session.headers = {
        'Accept': '*/*',
        'Referer': mms_base_uri + 'DataManager.xap?ignore={:%m-%d-%Y %H:%M:%S %p}'.format(datetime.now()),
        'Accept-Language': 'en-US',
        # 'Content-Length': str(len(request)),
        'Content-Type': 'text/xml; charset=utf-8',
        # 'SOAPAction': 'http://' + soap_action,
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; McAfee; InfoPath.2)',
        'Host': 'fpc27536s1',
        'DNT': '1',
        'Connection': 'Keep-Alive',
        'Cache-Control': 'no-cache'
    }

    transport = Transport(cache=SqliteCache(), session=session)

    return Client(
        'http://fpc27536s1/MMS5/Services/%sService.svc?wsdl' % service,
        transport=transport)


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


@bp.route('')
def service_list():
    services = [s for s in vars(Services) if not s.startswith('__') and s is not 'dump']
    services.sort()
    return render_template('services.html', services=services)


@bp.route('/<service>')
def service(service):
    return render_template('wsdl.html', service=service, wsdl=Services.dump(service))
