from fastems import services

class PalletService(services.FastemsService):
    def __init__(self):
        super().__init__('PalletService')

    def AddFixtureToFixturePosition(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:ModifyFixturePositionContentRequestDto']'''
        return self._client.service.AddFixtureToFixturePosition(requestor, request)

    def ChangePalletLocation(self, requestor, palletId, fromLocation, toLocation):
        '''['requestor: ns2:RequestorDto', 'palletId: ns3:PalletIdentityDto', 'fromLocation: xsd:string', 'toLocation: xsd:string']'''
        return self._client.service.ChangePalletLocation(requestor, palletId, fromLocation, toLocation)

    def CreatePallet(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:CreatePalletRequestDto']'''
        return self._client.service.CreatePallet(requestor, request)

    def DeleteFixturePosition(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:FixturePositionDeleteRequestDto']'''
        return self._client.service.DeleteFixturePosition(requestor, request)

    def DeletePallet(self, requestor, palletId):
        '''['requestor: ns2:RequestorDto', 'palletId: ns3:PalletIdentityDto']'''
        return self._client.service.DeletePallet(requestor, palletId)

    def GetAvailablePalletLocations(self, palletTypeId, dimensions):
        '''['palletTypeId: ns4:guid', 'dimensions: ns3:PalletNominalDimensionsDto']'''
        return self._client.service.GetAvailablePalletLocations(palletTypeId, dimensions)

    def GetAvailablePalletNumbers(self, palletTypeId, dimensions):
        '''['palletTypeId: ns3:PalletTypeIdentityDto', 'dimensions: ns3:PalletNominalDimensionsDto']'''
        return self._client.service.GetAvailablePalletNumbers(palletTypeId, dimensions)

    def GetPalletLocationsAcceptingPalletType(self, palletType):
        '''['palletType: xsd:string']'''
        return self._client.service.GetPalletLocationsAcceptingPalletType(palletType)

    def ModifyPart(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:ModifyPartRequestDto']'''
        return self._client.service.ModifyPart(requestor, request)

    def MovePart(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:MovePartRequestDto']'''
        return self._client.service.MovePart(requestor, request)

    def RemoveFixtureFromFixturePosition(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:ModifyFixturePositionContentRequestDto']'''
        return self._client.service.RemoveFixtureFromFixturePosition(requestor, request)

    def ResetMaterialPalletError(self, requestor, palletId):
        '''['requestor: ns2:RequestorDto', 'palletId: ns3:PalletIdentityDto']'''
        return self._client.service.ResetMaterialPalletError(requestor, palletId)

    def ResetPalletTimer(self, requestor, palletId):
        '''['requestor: ns2:RequestorDto', 'palletId: ns3:PalletIdentityDto']'''
        return self._client.service.ResetPalletTimer(requestor, palletId)

    def SaveFixturePosition(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:FixturePositionSaveRequestDto']'''
        return self._client.service.SaveFixturePosition(requestor, request)

    def ScrapParts(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:ScrapPartsRequestDto']'''
        return self._client.service.ScrapParts(requestor, request)

    def SetPalletDeviceCommands(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:SetPalletDeviceCommandsRequestDto']'''
        return self._client.service.SetPalletDeviceCommands(requestor, request)

    def SetPalletTimer(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:SetPalletTimerRequestDto']'''
        return self._client.service.SetPalletTimer(requestor, request)

    def UpdateMaterialPalletFullState(self, requestor, palletId, isFull):
        '''['requestor: ns2:RequestorDto', 'palletId: ns3:PalletIdentityDto', 'isFull: xsd:boolean']'''
        return self._client.service.UpdateMaterialPalletFullState(requestor, palletId, isFull)

    def UpdatePallet(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:UpdatePalletRequestDto']'''
        return self._client.service.UpdatePallet(requestor, request)


