from fastems import services

class WorkplaceService(services.FastemsService):
    def __init__(self):
        super().__init__('WorkplaceService')

    def CancelManualOperation(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns4:EndManualOperationDto']'''
        return self._client.service.CancelManualOperation(requestor, request)

    def EndManualOperation(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns4:EndManualOperationDto']'''
        return self._client.service.EndManualOperation(requestor, request)

    def GetWorkplaces(self):
        ''''''
        return self._client.service.GetWorkplaces()

    def IsManualOperationsEnabled(self):
        ''''''
        return self._client.service.IsManualOperationsEnabled()

    def SaveActiveSetting(self, requestor, workplaceName, workUnitName, activeSetting):
        '''['requestor: ns2:RequestorDto', 'workplaceName: xsd:string', 'workUnitName: xsd:string', 'activeSetting: xsd:string']'''
        return self._client.service.SaveActiveSetting(requestor, workplaceName, workUnitName, activeSetting)

    def SaveWorkUnitSettings(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns4:SaveWorkUnitSettingsDto']'''
        return self._client.service.SaveWorkUnitSettings(requestor, request)

    def ScrapManualOperation(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns4:EndManualOperationDto']'''
        return self._client.service.ScrapManualOperation(requestor, request)

    def StartManualOperation(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns4:StartManualOperationDto']'''
        return self._client.service.StartManualOperation(requestor, request)


