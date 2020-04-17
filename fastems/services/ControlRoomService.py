from fastems import services

class ControlRoomService(services.FastemsService):
    def __init__(self):
        super().__init__('ControlRoomService')

    def GetControlRooms(self):
        ''''''
        return self._client.service.GetControlRooms()


