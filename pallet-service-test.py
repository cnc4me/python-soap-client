import json

from zeep.exceptions import Fault

from services.PalletService import PalletService

if __name__ == '__main__':
    try:
        print(PalletService())

        params = PalletService().GetPalletTypes()

        print(params)

    except Fault as e:
        print(e.detail)
