from fastems import services

class ProductionSchedulerService(services.FastemsService):
    def __init__(self):
        super().__init__('ProductionSchedulerService')

    def CompletePalletProcessSteps(self, requestor, requests):
        '''['requestor: ns2:RequestorDto', 'requests: ns3:ArrayOfProcessStepActionRequestDto']'''
        return self._client.service.CompletePalletProcessSteps(requestor, requests)

    def CompletePalletRouteSteps(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns9:RouteStepActionRequestDto']'''
        return self._client.service.CompletePalletRouteSteps(requestor, request)

    def DeletePalletRoute(self, requestor, palletId):
        '''['requestor: ns2:RequestorDto', 'palletId: ns5:PalletIdentityDto']'''
        return self._client.service.DeletePalletRoute(requestor, palletId)

    def GetDeviceSettings(self, deviceId):
        '''['deviceId: ns2:EntityIdDto']'''
        return self._client.service.GetDeviceSettings(deviceId)

    def GetProductionDevices(self):
        ''''''
        return self._client.service.GetProductionDevices()

    def GetSettings(self):
        ''''''
        return self._client.service.GetSettings()

    def ReleasePallet(self, requestor, palletId):
        '''['requestor: ns2:RequestorDto', 'palletId: ns5:PalletIdentityDto']'''
        return self._client.service.ReleasePallet(requestor, palletId)

    def ResetPalletProcessSteps(self, requestor, requests):
        '''['requestor: ns2:RequestorDto', 'requests: ns3:ArrayOfProcessStepActionRequestDto']'''
        return self._client.service.ResetPalletProcessSteps(requestor, requests)

    def ResetPalletRouteSteps(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns9:RouteStepActionRequestDto']'''
        return self._client.service.ResetPalletRouteSteps(requestor, request)

    def SaveDeviceSettings(self, requestor, deviceId, settings):
        '''['requestor: ns2:RequestorDto', 'deviceId: ns2:EntityIdDto', 'settings: ns3:DeviceScheduleSettingsDto']'''
        return self._client.service.SaveDeviceSettings(requestor, deviceId, settings)

    def SavePalletRoute(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns9:PalletRouteSaveRequestDto']'''
        return self._client.service.SavePalletRoute(requestor, request)

    def SaveSettings(self, requestor, settings):
        '''['requestor: ns2:RequestorDto', 'settings: ns3:SchedulingSettingsDto']'''
        return self._client.service.SaveSettings(requestor, settings)

    def SetPalletDummyMode(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:PalletDummyModeRequestDto']'''
        return self._client.service.SetPalletDummyMode(requestor, request)

    def SetPalletRoutingMode(self, requestor, palletId, mode):
        '''['requestor: ns2:RequestorDto', 'palletId: ns5:PalletIdentityDto', 'mode: ns5:PalletRoutingModeDto']'''
        return self._client.service.SetPalletRoutingMode(requestor, palletId, mode)

    def SetPalletToolCheckMode(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:PalletToolCheckModeSetRequestDto']'''
        return self._client.service.SetPalletToolCheckMode(requestor, request)

    def SuspendPallet(self, requestor, palletId):
        '''['requestor: ns2:RequestorDto', 'palletId: ns5:PalletIdentityDto']'''
        return self._client.service.SuspendPallet(requestor, palletId)

    def UpdateSchedule(self, requestor):
        '''['requestor: ns2:RequestorDto']'''
        return self._client.service.UpdateSchedule(requestor)


