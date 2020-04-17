from fastems import services

class FadectorService(services.FastemsService):
    def __init__(self):
        super().__init__('FadectorService')

    def GetDeviceStatusClassificationCodes(self):
        ''''''
        return self._client.service.GetDeviceStatusClassificationCodes()

    def GetFullDeviceStatusEntry(self, entryId):
        '''['entryId: ns7:guid']'''
        return self._client.service.GetFullDeviceStatusEntry(entryId)

    def GetOeeDevicesForOperationStep(self, part, order, operation, step):
        '''['part: xsd:string', 'order: xsd:string', 'operation: xsd:string', 'step: xsd:int']'''
        return self._client.service.GetOeeDevicesForOperationStep(part, order, operation, step)

    def GetOeeStepsForOperation(self, part, order, operation):
        '''['part: xsd:string', 'order: xsd:string', 'operation: xsd:string']'''
        return self._client.service.GetOeeStepsForOperation(part, order, operation)

    def GetScrapReasonCodes(self):
        ''''''
        return self._client.service.GetScrapReasonCodes()

    def SaveDeviceStatusEntry(self, requestor, entry):
        '''['requestor: ns2:RequestorDto', 'entry: ns5:DeviceStatusEntryDto']'''
        return self._client.service.SaveDeviceStatusEntry(requestor, entry)


