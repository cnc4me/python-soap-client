import csv
import json
import re
from datetime import datetime

from fastems.job import Job


class Schedule(object):
    DATETIME_PARSE_FORMATS = (
        '%m/%d',
        '%m/%d/%Y',
        '%m/%d/%Y %H:%M:%S'
    )

    def __init__(self, csv_path: str):
        self._csv_path = csv_path

    def _parse_date(self, datetime_str: str):
        dt = None

        for f in self.DATETIME_PARSE_FORMATS:
            try:
                dt = datetime.strptime(datetime_str, f)

                if dt.year < 2000:
                    dt = dt.replace(year=datetime.now().year)
            except ValueError:
                pass

            if dt is not None:
                return dt

        return None

    def _normalize(self, row):
        headings = {
            'R/T . / Kanban': 'order_number',
            'Part .': 'part_number',
            'Job . / Name': 'description',
            # 'Description': 'description',
            'Run Qty': 'qty',
            'Due Date': 'due_date',
            'Notes': 'notes'
        }

        new_row = {headings[col]: row[col] for col in list(headings)}

        # new_row['description'] = '[%s] %s' % (new_row['part_number'], new_row['description'])
        # new_row['status'] = 'Planned'
        # new_row['start_date'] = datetime.now().isoformat()
        new_row['qty'] = int(float(new_row['qty']))
        new_row['parsed_due_date'] = self._parse_date(new_row['due_date'])
        new_row['notes_due_date'] = None

        try:
            match = re.findall('([0-9]+/[0-9]+(?:/[0-9]+)?)', new_row['notes'])

            new_row['notes_due_date'] = self._parse_date(match[0])
            new_row['due_date'] = new_row['notes_due_date']
        except Exception as e:
            pass

        if new_row['due_date'] is None:
            new_row['due_date'] = new_row['parsed_due_date']

        del new_row['parsed_due_date']
        del new_row['notes_due_date']
        del new_row['notes']

        return new_row

    def get_all(self):
        with open(self._csv_path) as file:
            return [self._normalize(row) for row in csv.DictReader(file)]


if __name__ == '__main__':
    import config

    s = Schedule(config.SCHEDULE_CSV_PATH)

    print(json.dumps(s.get_all(), indent=2))
