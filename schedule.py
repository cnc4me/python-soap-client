import csv
import re

import utils
import fastemsdate

schedule_csv_path = 'C:/Users/kevinh/ownCloud/Schedules/A17.csv'


def get_scheduled_work():
    with open(schedule_csv_path) as file:
        reader = csv.DictReader(file)
        return [_normalize(row) for row in reader]


def _normalize(row):
    headings = {
        'R/T . / Kanban': 'order_number',
        'Part .': 'part_number',
        'Description': 'description',
        'Run Qty': 'quantity',
        'Due Date': 'due_date',
        'Notes': 'notes'
    }

    new_row = {headings[col]: row[col] for col in list(headings)}

    new_row['description'] = '[%s] %s' % (new_row['part_number'], new_row['description'])
    new_row['status'] = 'Planned'
    new_row['start_date'] = fastemsdate.start_now()
    new_row['quantity'] = int(float(new_row['quantity']))
    new_row['due_date'] = fastemsdate.parse(new_row['due_date'])
    new_row['notes_due_date'] = None

    try:
        match = re.findall('([0-9]+/[0-9]+(?:/[0-9]+)?)', new_row['notes'])

        new_row['notes_due_date'] = fastemsdate.parse(match[0])
        new_row['due_date'] = new_row['notes_due_date']
        del new_row['notes_due_date']
    except Exception as e:
        pass

    del new_row['notes']

    return new_row


if __name__ == '__main__':
    utils.print_json(get_scheduled_work())
