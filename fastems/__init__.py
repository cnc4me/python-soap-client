import shelve
from datetime import datetime, timedelta
from os import path

from .services import BaseDataService

__all__ = ['job', 'order', 'services']

gid_cache = path.join(path.dirname(path.abspath(__file__)), '../cache/gids')


def _get_base_data() -> list:
    response = BaseDataService().GetItemBaseData()
    return response['Data']['ItemBaseDataDto']


def get_base_data() -> list:
    with shelve.open(gid_cache) as cache:
        now = datetime.now()
        expires = now + timedelta(hours=1)

        if 'expires' not in cache:
            cache['expires'] = expires

        if 'gids' not in cache:
            cache['gids'] = _get_base_data()

        if cache['expires'] < now:
            cache['expires'] = expires
            return _get_base_data()
        else:
            return cache['gids']


def get_part_number_to_gid_dict() -> dict:
    return {i['Name']: i['Id'] for i in get_base_data()}


def get_gid_for_part_number(part_number: str) -> str:
    pn_gid_map = get_part_number_to_gid_dict()

    if part_number not in pn_gid_map:
        raise KeyError('Fastems did not return a GID for the part number "%s"' % part_number)

    return pn_gid_map[part_number]
