from zeep import xsd
from zeep.exceptions import Fault

from fastems.services.QueryService import QueryService

if __name__ == '__main__':
    any = xsd.AnyObject(xsd.AnyType(), None)

    try:
        orders = QueryService().RunQuery({
            'Parameters':[],
            'QueryName':'FetchOrderSummaries',
            'TopicName':'05f0b376-d8cd-445a-816a-5364ef34ec98'
        })

        print(orders)

    except Fault as e:
        print(e.detail)


