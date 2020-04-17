from fastems import services

class DeviceService(services.FastemsService):
    def __init__(self):
        super().__init__('DeviceService')

    def ChangeMachineChangerState(self, requestor, machine, request):
        '''['requestor: ns2:RequestorDto', 'machine: ns2:EntityIdDto', 'request: ns3:MachineChangerStateChangeRequestDto']'''
        return self._client.service.ChangeMachineChangerState(requestor, machine, request)

    def ClearToolChipData(self, requestor, chipReader, tool, deleteInstance):
        '''['requestor: ns2:RequestorDto', 'chipReader: ns2:EntityIdDto', 'tool: ns15:ToolIdentityDto', 'deleteInstance: xsd:boolean']'''
        return self._client.service.ClearToolChipData(requestor, chipReader, tool, deleteInstance)

    def DecreaseDeviceOverridePercent(self, requestor, device):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto']'''
        return self._client.service.DecreaseDeviceOverridePercent(requestor, device)

    def GetAccessibleCtsTransportDeviceSourceLocations(self, device):
        '''['device: ns2:EntityIdDto']'''
        return self._client.service.GetAccessibleCtsTransportDeviceSourceLocations(device)

    def GetAccessibleCtsTransportDeviceTargetLocations(self, device, toolId):
        '''['device: ns2:EntityIdDto', 'toolId: ns15:ToolIdentityDto']'''
        return self._client.service.GetAccessibleCtsTransportDeviceTargetLocations(device, toolId)

    def GetAccessiblePalletTransportDeviceSourceLocations(self, device):
        '''['device: ns2:EntityIdDto']'''
        return self._client.service.GetAccessiblePalletTransportDeviceSourceLocations(device)

    def GetAccessiblePalletTransportDeviceTargetLocations(self, device, palletId):
        '''['device: ns2:EntityIdDto', 'palletId: ns8:PalletIdentityDto']'''
        return self._client.service.GetAccessiblePalletTransportDeviceTargetLocations(device, palletId)

    def GetDevices(self):
        ''''''
        return self._client.service.GetDevices()

    def GetPalletTransportDeviceXYTaskTargetLocations(self, device, loadType):
        '''['device: ns2:EntityIdDto', 'loadType: xsd:string']'''
        return self._client.service.GetPalletTransportDeviceXYTaskTargetLocations(device, loadType)

    def IncreaseDeviceOverridePercent(self, requestor, device):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto']'''
        return self._client.service.IncreaseDeviceOverridePercent(requestor, device)

    def ModifyHydraulicLine(self, requestor, loadingStation, request):
        '''['requestor: ns2:RequestorDto', 'loadingStation: ns2:EntityIdDto', 'request: ns8:ModifyHydraulicLineRequestDto']'''
        return self._client.service.ModifyHydraulicLine(requestor, loadingStation, request)

    def Recover(self, requestor, device, errorRecoveryOperation):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto', 'errorRecoveryOperation: xsd:string']'''
        return self._client.service.Recover(requestor, device, errorRecoveryOperation)

    def RequestAutopilotModeOff(self, requestor, device):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto']'''
        return self._client.service.RequestAutopilotModeOff(requestor, device)

    def RequestAutopilotModeOn(self, requestor, device):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto']'''
        return self._client.service.RequestAutopilotModeOn(requestor, device)

    def RequestCaptureImage(self, requestor, device):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto']'''
        return self._client.service.RequestCaptureImage(requestor, device)

    def RequestCreateCtsRobotTransportTask(self, requestor, robot, request):
        '''['requestor: ns2:RequestorDto', 'robot: ns2:EntityIdDto', 'request: ns3:CreateCtsTransportTaskRequestDto']'''
        return self._client.service.RequestCreateCtsRobotTransportTask(requestor, robot, request)

    def RequestIOConveyorModeChange(self, requestor, ioConveyor, mode):
        '''['requestor: ns2:RequestorDto', 'ioConveyor: ns2:EntityIdDto', 'mode: ns3:IOConveyorModeDto']'''
        return self._client.service.RequestIOConveyorModeChange(requestor, ioConveyor, mode)

    def RequestPalletTransportDeviceDriveXY(self, requestor, device, request):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto', 'request: ns3:DriveXYRequestDto']'''
        return self._client.service.RequestPalletTransportDeviceDriveXY(requestor, device, request)

    def RequestPalletTransportDeviceMovePallet(self, requestor, device, request):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto', 'request: ns3:MovePalletRequestDto']'''
        return self._client.service.RequestPalletTransportDeviceMovePallet(requestor, device, request)

    def RequestRobotProgramState(self, requestor, robot, state):
        '''['requestor: ns2:RequestorDto', 'robot: ns2:EntityIdDto', 'state: ns3:RobotProgramStateDto']'''
        return self._client.service.RequestRobotProgramState(requestor, robot, state)

    def ResetAlarms(self, requestor, device):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto']'''
        return self._client.service.ResetAlarms(requestor, device)

    def SetCraneManualDriveSettings(self, requestor, crane, settings):
        '''['requestor: ns2:RequestorDto', 'crane: ns2:EntityIdDto', 'settings: ns3:CraneManualDriveSettingsDto']'''
        return self._client.service.SetCraneManualDriveSettings(requestor, crane, settings)

    def SetDeviceOverridePercent(self, requestor, device, overridePercent):
        '''['requestor: ns2:RequestorDto', 'device: ns2:EntityIdDto', 'overridePercent: xsd:int']'''
        return self._client.service.SetDeviceOverridePercent(requestor, device, overridePercent)

    def WriteToolChipData(self, requestor, chipReader, tool):
        '''['requestor: ns2:RequestorDto', 'chipReader: ns2:EntityIdDto', 'tool: ns15:ToolIdentityDto']'''
        return self._client.service.WriteToolChipData(requestor, chipReader, tool)


