import random
import sys
import time

from colorama import Back, Fore, Style, init

import config
from fastems.job import job_factory
from fastems.order import PlannedOrder
from schedule import Schedule


fail = {
    'Success':'False',
    'Message': {
        'Text':'Order number {1} was not created for {0}'
    }
}

success = {
    'Success': 'True'
}


def fprint(s):
    print(s, flush=True)


if __name__ == '__main__':
    init(strip=False)

    fprint(Back.BLUE+Fore.BLACK)
    fprint('     _________   ___________________  ________    ____  ____  ____  __________     __________  _________  __________  ____  ')
    fprint('    / ____/   | / ___/_  __/ ____/  |/  / ___/   / __ \/ __ \/ __ \/ ____/ __ \   / ____/ __ \/ ____/   |/_  __/ __ \/ __ \ ')
    fprint('   / /_  / /| | \__ \ / / / __/ / /|_/ /\__ \   / / / / /_/ / / / / __/ / /_/ /  / /   / /_/ / __/ / /| | / / / / / / /_/ / ')
    fprint('  / __/ / ___ |___/ // / / /___/ /  / /___/ /  / /_/ / _, _/ /_/ / /___/ _, _/  / /___/ _, _/ /___/ ___ |/ / / /_/ / _, _/  ')
    fprint(' /_/   /_/  |_/____//_/ /_____/_/  /_//____/   \____/_/ |_/_____/_____/_/ |_|   \____/_/ |_/_____/_/  |_/_/  \____/_/ |_|   ')
    fprint('                                                                                                                            ')
    fprint(Style.RESET_ALL + '')

    try:
        fprint(Fore.CYAN+'[INFO] Reading and parsing schedule CSV...')
        access_schedule = Schedule(config.SCHEDULE_CSV_PATH)
    except PermissionError as e:
        fprint(Fore.RED+'There was an error when reading the from %s' % config.SCHEDULE_CSV_PATH)
        fprint('[ERROR] %s' % str(e))
        sys.exit()

    fprint(Fore.GREEN+'...Done!')
    fprint('')

    for job_details in access_schedule.get_all():
        fprint('')
        fprint(Fore.CYAN+'[INFO] Creating job from schedule details for %s' % job_details['part_number'])

        try:
            job = job_factory(**job_details)
            fprint(Fore.BLUE+'[FASTEMS] The GID for %s is %s' % (job.part_number, job.gid))
            fprint(Fore.CYAN+'[INFO] Created Order %s for %s' % (job.order_number, job.description))
            fprint('[INFO] Submitting Order to Fastems....')

            order = PlannedOrder(job)
            response = order.submit()
            # response = random.choice([success, fail])

            if response['Success']:
                msg = Fore.GREEN+'[SUCCESS] Order created successfully!'
            else:
                msg = Fore.RED+'[ERROR] %s' % response['Message']['Text']
                msg = msg.format(job_details['part_number'], job_details['order_number'])

            fprint(msg)
            time.sleep(.5)
        except KeyError as e:
            fprint(Fore.RED+'[ERROR] Fastems did not return a GID for %s; Skipping...' % job_details['part_number'])
