#!/Users/kevinh/.virtualenvs/fastems-bridge/Scripts/python

import sys

sys.stdout = sys.stderr
sys.path.insert(0, "C:/Users/kevinh/projects/harris-bruno/apps/fastems-bridge")

# noinspection PyUnresolvedReferences
from app import app as application
