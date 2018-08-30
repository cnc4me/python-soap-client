from fastems import services

class QueryService(services.FastemsService):
    def __init__(self):
        super().__init__('QueryService')

    def RunQuery(self, ticket):
        '''['ticket: ns2:QueryTicketDto']'''
        return self._client.service.RunQuery(ticket)


