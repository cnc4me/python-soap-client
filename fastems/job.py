from datetime import datetime

import fastems


class Job(object):
    def __init__(self, part_number: str, order_number, description: str, qty: int,
                 due_date: datetime, start_date: datetime = None):
        self.qty = qty
        self.gid = None
        self.due_date = due_date
        self.description = description
        self.order_number = order_number
        self.part_number = part_number.upper()
        self.start_date = datetime.now() if start_date is None else start_date


def job_factory(part_number: str, order_number, description: str, qty: int,
                 due_date: datetime, start_date: datetime = None):

    new_job = Job(part_number, order_number, description, qty, due_date, start_date)
    new_job.gid = fastems.get_gid_for_part_number(new_job.part_number)
    return new_job

if __name__ == '__main__':
    from datetime import date
    from random import randint

    job_data = {
        'description': 'Fastems Bridge Order Creation Test',
        'order_number': 99999,
        'qty': randint(10000, 90000),
        'due_date': date(2018, 8, 29)
    }

    job = Job('HB96-15', **job_data)

    print(job.__dict__)
