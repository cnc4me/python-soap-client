from fastems import services

class ToolService(services.FastemsService):
    def __init__(self):
        super().__init__('ToolService')

    def AdministrativeChangeToolLocation(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns13:ToolLocationChangeRequestDto']'''
        return self._client.service.AdministrativeChangeToolLocation(requestor, request)

    def AdministrativeMobilizeToolsRequest(self, requestor, requests):
        '''['requestor: ns2:RequestorDto', 'requests: ns13:ArrayOfToolMobilizationRequestDto']'''
        return self._client.service.AdministrativeMobilizeToolsRequest(requestor, requests)

    def CreateToolPresettingRequest(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns9:ToolPresettingRequestSaveRequestDto']'''
        return self._client.service.CreateToolPresettingRequest(requestor, request)

    def DeleteMagazinePlanningSet(self, requestor, identity):
        '''['requestor: ns2:RequestorDto', 'identity: ns14:MagazinePlanningSetIdentityDto']'''
        return self._client.service.DeleteMagazinePlanningSet(requestor, identity)

    def DeleteStandardToolMagazine(self, requestor, standardToolMagazineId):
        '''['requestor: ns2:RequestorDto', 'standardToolMagazineId: ns5:guid']'''
        return self._client.service.DeleteStandardToolMagazine(requestor, standardToolMagazineId)

    def DeleteToolBaseData(self, requestor, baseDataId):
        '''['requestor: ns2:RequestorDto', 'baseDataId: ns5:guid']'''
        return self._client.service.DeleteToolBaseData(requestor, baseDataId)

    def DeleteToolInstance(self, requestor, toolId):
        '''['requestor: ns2:RequestorDto', 'toolId: ns5:guid']'''
        return self._client.service.DeleteToolInstance(requestor, toolId)

    def DeleteToolPresettingRequest(self, requestor, requestId):
        '''['requestor: ns2:RequestorDto', 'requestId: ns5:guid']'''
        return self._client.service.DeleteToolPresettingRequest(requestor, requestId)

    def ExecuteMagazinePlanning(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns14:ToolMagazinePlanningRequestDto']'''
        return self._client.service.ExecuteMagazinePlanning(requestor, request)

    def GetAllowedToolLocationNames(self, baseDataIdentity, includeOccupied):
        '''['baseDataIdentity: ns10:ToolBaseDataIdentityDto', 'includeOccupied: xsd:boolean']'''
        return self._client.service.GetAllowedToolLocationNames(baseDataIdentity, includeOccupied)

    def GetReservedSisterNumbers(self, baseDataIdentity):
        '''['baseDataIdentity: ns10:ToolBaseDataIdentityDto']'''
        return self._client.service.GetReservedSisterNumbers(baseDataIdentity)

    def GetToolReservations(self, toolIds):
        '''['toolIds: ns11:ArrayOfguid']'''
        return self._client.service.GetToolReservations(toolIds)

    def SaveMagazinePlanningSet(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns14:MagazinePlanningSetSaveRequestDto']'''
        return self._client.service.SaveMagazinePlanningSet(requestor, request)

    def SaveStandardToolMagazine(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns4:StandardToolMagazineSaveRequestDto']'''
        return self._client.service.SaveStandardToolMagazine(requestor, request)

    def SaveToolBaseData(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns10:SaveToolBaseDataRequestDto']'''
        return self._client.service.SaveToolBaseData(requestor, request)

    def SaveToolInstance(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns8:SaveToolInstanceRequestDto']'''
        return self._client.service.SaveToolInstance(requestor, request)

    def SetPresettingRequestTools(self, requestor, binding):
        '''['requestor: ns2:RequestorDto', 'binding: ns9:PresettingRequestToolBindingDto']'''
        return self._client.service.SetPresettingRequestTools(requestor, binding)

    def SetToolMovingAllowanceRequest(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns13:ToolMovingAllowanceRequestDto']'''
        return self._client.service.SetToolMovingAllowanceRequest(requestor, request)


