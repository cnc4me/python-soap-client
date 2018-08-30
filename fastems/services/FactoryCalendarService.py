from fastems import services

class FactoryCalendarService(services.FastemsService):
    def __init__(self):
        super().__init__('FactoryCalendarService')

    def DeleteFactoryExceptionDay(self, requestor, day):
        '''['requestor: ns2:RequestorDto', 'day: ns3:FactoryExceptionDayDto']'''
        return self._client.service.DeleteFactoryExceptionDay(requestor, day)

    def UpdateFactoryDays(self, requestor, days):
        '''['requestor: ns2:RequestorDto', 'days: ns3:ArrayOfFactoryDayDto']'''
        return self._client.service.UpdateFactoryDays(requestor, days)

    def UpdateFactoryExceptionDay(self, requestor, day):
        '''['requestor: ns2:RequestorDto', 'day: ns3:FactoryExceptionDayDto']'''
        return self._client.service.UpdateFactoryExceptionDay(requestor, day)


