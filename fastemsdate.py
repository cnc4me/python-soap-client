import json
from datetime import datetime, timedelta

import utils

FASTEMS_ORDER_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
FASTEMS_IGNORE_FORMAT = '%m-%d-%Y %H:%M:%S %p'
DATETIME_PARSE_FORMATS = (
    '%m/%d',
    '%m/%d/%Y',
    '%m/%d/%Y %H:%M:%S'
)


def parse(datetime_str: str):
    dt = None

    for f in DATETIME_PARSE_FORMATS:
        try:
            dt = datetime.strptime(datetime_str, f)

            if dt.year < 2000:
                dt = dt.replace(year=datetime.now().year)

        except ValueError:
            pass

    return to_string(dt) if dt is not None else None


def to_string(dt: datetime):
    return dt.strftime(FASTEMS_ORDER_FORMAT)


def start_now():
    return to_string(datetime.now())


def add_days(dt, days):
    return to_string(dt + timedelta(days=days))


def days_from_now(days):
    return add_days(datetime.now(), days)

if __name__ == '__main__':
    fd = to_string(datetime.now())

    utils.print_json(fd)
