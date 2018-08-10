from random import randint

import fastems
import fastemsdate
import utils

order_times_format = '%Y-%m-%dT%H:%M:%SZ'

test_data = [
    {
        "gid": "23df5c6a-3c6b-4c9f-81fd-a72200ab314e",
        "part_number": "8084-3-159-02"
    },
    {
        "gid": "bb4f0dd3-dc54-4fed-8e10-a72200899552",
        "part_number": "HB465-20"
    },
    {
        "gid": "f6143172-4b03-4ac3-a7a4-a6be006ce7e6",
        "part_number": "7951MS-1-12"
    },
    {
        "gid": "a0f77636-8ca6-4893-8aa4-a6be006a14b7",
        "part_number": "8029-3-296"
    }
]

order_num = 999990

for part_data in test_data:
    order_data = {
        'gid': part_data['gid'],
        'part_number': part_data['part_number'],
        'description': 'Batch Order Creation Test',
        'order_number': order_num,
        'quantity': randint(5000000, 6000000),
        'status': 'Planned',
        'start_date': fastemsdate.start_now(),
        'due_date': fastemsdate.days_from_now(5)
    }

    order_num += 1

    response = fastems.create_order(order_data)
    result = utils.parse_response(response)['CreateOrderResponse']

    print(result)
