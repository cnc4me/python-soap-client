from fastems import services

class OrderService(services.FastemsService):
    def __init__(self):
        super().__init__('OrderService')

    def BookScrapParts(self, requestor, scrapRequest):
        '''['requestor: ns2:RequestorDto', 'scrapRequest: ns3:BookScrapPartRequestDto']'''
        return self._client.service.BookScrapParts(requestor, scrapRequest)

    def CreateOrder(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:CreateOrderRequestDto']'''
        return self._client.service.CreateOrder(requestor, request)

    def DeleteCompletedOrders(self, requestor):
        '''['requestor: ns2:RequestorDto']'''
        return self._client.service.DeleteCompletedOrders(requestor)

    def DeleteOrder(self, requestor, orderId):
        '''['requestor: ns2:RequestorDto', 'orderId: ns3:OrderIdentityDto']'''
        return self._client.service.DeleteOrder(requestor, orderId)

    def GetOrders(self, ids):
        '''['ids: ns7:ArrayOfguid']'''
        return self._client.service.GetOrders(ids)

    def GetOrdersForOperation(self, operationId):
        '''['operationId: ns4:guid']'''
        return self._client.service.GetOrdersForOperation(operationId)

    def SaveSettings(self, requestor, settings):
        '''['requestor: ns2:RequestorDto', 'settings: ns3:OrderSettingsDto']'''
        return self._client.service.SaveSettings(requestor, settings)

    def UpdateOrder(self, requestor, request):
        '''['requestor: ns2:RequestorDto', 'request: ns3:UpdateOrderRequestDto']'''
        return self._client.service.UpdateOrder(requestor, request)


