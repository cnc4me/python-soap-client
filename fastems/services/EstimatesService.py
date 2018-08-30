from fastems import services

class EstimatesService(services.FastemsService):
    def __init__(self):
        super().__init__('EstimatesService')

    def CalculateEstimates(self, request):
        '''['request: ns2:EstimateCalculationRequestDto']'''
        return self._client.service.CalculateEstimates(request)


