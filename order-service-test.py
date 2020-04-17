from datetime import date
from random import randint

import fastems
from fastems.job import job_factory
from fastems.order import PlannedOrder
from fastems.services.OrderService import OrderService


def get_orders():
    gids = [
        i['Id'] for i in fastems.get_base_data()
    ]

    return OrderService().GetOrders([''])


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

    return work_order.submit()


if __name__ == '__main__':
    try:
        response = get_orders()

        print(response)
    except Exception as e:
        print(str(e))
