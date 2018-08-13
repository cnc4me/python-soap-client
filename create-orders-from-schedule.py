from time import sleep

import fastems
import schedule
import utils

print('+--------------------------+', flush=True)
print('|      Fastems Bridge      |', flush=True)
print('+--------------------------+', flush=True)
print('', flush=True)

print('Fetching GIDs from Fastems...', flush=True)
gid_map = fastems.get_part_number_to_gid_dict()
print('Done!', flush=True)
print('', flush=True)

print('Reading and parsing schedule CSV...', flush=True)
try:
    scheduled_work = schedule.get_scheduled_work()
    print('Done!', flush=True)
    print('', flush=True)

    for router in scheduled_work:
        if router['part_number'] in gid_map:
            router['gid'] = gid_map[router['part_number']]

            # print(repr(router))
            print('|', flush=True)
            print('| Found GID[{gid}] for {part_number}'.format(**router), flush=True)
            print('+--> Creating order for RT#{order_number} - {description}'.format(**router), flush=True)

            response = fastems.create_order(router)
            result = utils.parse_response(response)['CreateOrderResponse']['CreateOrderResult']

            if result['Success'] == 'False':
                msg = '|----> ' + result['Message']['Text']
                msg = msg.format(router['part_number'], router['order_number'])
            else:
                msg = '|----> Success!'

            print(msg, flush=True)
            sleep(.5)
except PermissionError as e:
    print('There was an error when reading the CSV file.', flush=True)
    print('[ERROR] %s' % str(e), flush=True)
