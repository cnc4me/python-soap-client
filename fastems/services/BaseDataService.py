from fastems import services

class BaseDataService(services.FastemsService):
    def __init__(self):
        super().__init__('BaseDataService')

    def DeleteFixture(self, requestor, fixtureId):
        '''['requestor: ns4:RequestorDto', 'fixtureId: ns5:FixtureBaseDataIdentityDto']'''
        return self._client.service.DeleteFixture(requestor, fixtureId)

    def DeleteItem(self, requestor, itemId):
        '''['requestor: ns4:RequestorDto', 'itemId: ns5:BaseDataIdentityDto']'''
        return self._client.service.DeleteItem(requestor, itemId)

    def DeleteProcessPlan(self, requestor, processPlanId):
        '''['requestor: ns4:RequestorDto', 'processPlanId: ns5:ProcessPlanIdentityDto']'''
        return self._client.service.DeleteProcessPlan(requestor, processPlanId)

    def GetFixtureBaseData(self, fixtureIds):
        '''['fixtureIds: ns2:ArrayOfguid']'''
        return self._client.service.GetFixtureBaseData(fixtureIds)

    def GetItemBaseData(self, itemIds):
        '''['itemIds: ns2:ArrayOfguid']'''
        return self._client.service.GetItemBaseData(itemIds)

    def GetManufacturedOperationIdsForFixture(self, fixtureId):
        '''['fixtureId: ns3:guid']'''
        return self._client.service.GetManufacturedOperationIdsForFixture(fixtureId)

    def GetOperationsUsingNcProgram(self, programId):
        '''['programId: ns7:NcProgramIdentityDto']'''
        return self._client.service.GetOperationsUsingNcProgram(programId)

    def GetProcessPlans(self, ids):
        '''['ids: ns2:ArrayOfguid']'''
        return self._client.service.GetProcessPlans(ids)

    def GetProcessPlansProducingItemOperations(self, itemId):
        '''['itemId: ns3:guid']'''
        return self._client.service.GetProcessPlansProducingItemOperations(itemId)

    def SaveFixture(self, requestor, fixture):
        '''['requestor: ns4:RequestorDto', 'fixture: ns5:FixtureBaseDataSummaryDto']'''
        return self._client.service.SaveFixture(requestor, fixture)

    def SaveItem(self, requestor, request):
        '''['requestor: ns4:RequestorDto', 'request: ns5:ItemBaseDataSaveRequestDto']'''
        return self._client.service.SaveItem(requestor, request)

    def SaveProcessPlan(self, requestor, processPlan):
        '''['requestor: ns4:RequestorDto', 'processPlan: ns5:ProcessPlanDto']'''
        return self._client.service.SaveProcessPlan(requestor, processPlan)


