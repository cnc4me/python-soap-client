from fastems.job import Job
from services import Requestor
from services.OrderService import OrderService


class Order(object):
    def __init__(self, job: Job, status):
        self._service = OrderService()

        self.job = job
        self.status = status
        self.request = None

        self._data = {
            'Status': self.status,
            'Quantity': self.job.qty,
            'Number': self.job.order_number,
            'Description': self.job.description,
            'ItemBaseDataId': {'Id': self.job.gid},
            'DueDate': {'Utc': self.job.due_date},
            'EarliestStart': {'Utc': self.job.start_date},
        }

    def submit(self):
        return self._service.CreateOrder(Requestor, self._data)

    def inspect_request(self):
        return self._service._history.last_sent

    def inspect_response(self):
        return self._service._history.last_received


class ReleasedOrder(Order):
    def __init__(self, job: Job):
        super().__init__(job, 'Released')


class PlannedOrder(Order):
    def __init__(self, job: Job):
        super().__init__(job, 'Planned')


class SuspendedOrder(Order):
    def __init__(self, job: Job):
        super().__init__(job, 'Suspended')


class CompletedOrder(Order):
    def __init__(self, job: Job):
        super().__init__(job, 'Completed')
