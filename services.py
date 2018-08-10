from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.cache import SqliteCache
from zeep.transports import Transport


def _get_client(service):
    session = Session()
    session.auth = HTTPBasicAuth('mmsuser', 'user')

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
