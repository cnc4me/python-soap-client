import json
import sys
from datetime import date, datetime, timedelta
from random import randint

from json import dumps
from bs4 import BeautifulSoup

import utils
from services import Services

mms_base_uri = 'http://fpc27536s1/MMS5/'

client = Services.Order

requestor = {
    'ApplicationName': 'DataManager',
    'HostName': 'cnc405-pc',
    'UserName': 'mmsuser'
}

request = {
    'Description': 'KANBAN',
    'DueDate': {
        'Utc': date(2018, 8, 14)
    },
    'EarliestStart': {
        'Utc': (date(2018, 8, 14) + timedelta(days=5))
    },
    'ItemBaseDataId': {
        "Id": "bb4f0dd3-dc54-4fed-8e10-a72200899552",
        "Name": "HB465-20"
    },
    'Number': 99999,
    'Quantity': randint(5000, 6000),
    'Status': 'Planned'
}

# x = client.create_message(client.service, 'CreateOrder', requestor=requestor, request=request)

response = client.service.CreateOrder(requestor, request)

print(response)
