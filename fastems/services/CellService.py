from fastems import services

class CellService(services.FastemsService):
    def __init__(self):
        super().__init__('CellService')

    def GetCells(self):
        ''''''
        return self._client.service.GetCells()


