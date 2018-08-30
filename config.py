import logging
from os import path

FASTEMS_HOSTNAME = 'fpc27536s1'

DATA_MANAGER_USER='mmsuser'
DATA_MANAGER_PASS='user'

SCHEDULE_CSV_PATH = 'C:/Users/kevinh/ownCloud/Schedules/A17.csv'

DEBUG = True
TESTING = False
TEMPLATES_AUTO_RELOAD = True
# sqlite :memory: identifier is the default if no filepath is present
# SQLALCHEMY_DATABASE_URI = 'sqlite://'
# SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'
LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOGGING_LOCATION = path.join(path.dirname(path.abspath(__file__)), 'logs/app.log')
LOGGING_LEVEL = logging.DEBUG
