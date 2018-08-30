from fastems import services

class RemoteAlarmService(services.FastemsService):
    def __init__(self):
        super().__init__('RemoteAlarmService')

    def SaveUserSettings(self, requestor, settings):
        '''['requestor: ns2:RequestorDto', 'settings: ns3:UserSettingsDto']'''
        return self._client.service.SaveUserSettings(requestor, settings)

    def SendTestMessages(self, requestor, username):
        '''['requestor: ns2:RequestorDto', 'username: xsd:string']'''
        return self._client.service.SendTestMessages(requestor, username)


