from datetime import date
from random import randint

import zeep
from zeep import xsd
from zeep.exceptions import Fault
from zeep.plugins import HistoryPlugin

from fastems import Services
from fastems.job import job_factory
from fastems.order import PlannedOrder


def create_order():

    job_data = {
        'part_number': 'HB96-15',
        'description': 'Fastems Bridge Order Creation Test',
        'order_number': 99999,
        'qty': randint(10000, 90000),
        'due_date': date(2018, 8, 29)
    }

    job = job_factory(**job_data)
    work_order = PlannedOrder(job)

    # print(work_order.__dict__)

    try:
        response = work_order.submit()

        print(response)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    history = HistoryPlugin()
    client = Services.Query
    client.plugins.append(history)

    any = xsd.AnyObject(xsd.AnyType(), None)

    try:
        orders = client.service.RunQuery({
            'ticket':{
                'Parameters':[any],
                'QueryName':'FetchOrderSummaries',
                'TopicName':'05f0b376-d8cd-445a-816a-5364ef34ec98'
            }
        })

        print(history.last_sent['envelope'])
        print(history.last_received['envelope'])
        print(orders)

    except Fault as e:
        print(e.detail)


