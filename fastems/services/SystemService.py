from fastems import services

class SystemService(services.FastemsService):
    def __init__(self):
        super().__init__('SystemService')

    def GetServices(self):
        ''''''
        return self._client.service.GetServices()


