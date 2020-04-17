from zeep.exceptions import Fault

from services.CellService import CellService

if __name__ == '__main__':
    try:
        print(CellService())

        cells = CellService().GetCells()

        parts = cells['Data']['CellDto'][0]['Slots']['PartSlotDto'][0]['Parts']['PartDto']

        orders = {p['OrderName']: p['Operation']['ItemName'] for p in parts}

        print([p['Operation']['ItemName'] for p in parts if p['Operation']['IsReady']])
        # print(json.dumps(orders, indent=4, sort_keys=True))

    except Fault as e:
        print(e.detail)
