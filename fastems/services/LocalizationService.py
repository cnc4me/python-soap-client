from fastems import services

class LocalizationService(services.FastemsService):
    def __init__(self):
        super().__init__('LocalizationService')

    def GetErrorInfo(self, locale, identifier):
        '''['locale: xsd:string', 'identifier: xsd:string']'''
        return self._client.service.GetErrorInfo(locale, identifier)

    def GetErrorInfoSummaries(self, locale):
        '''['locale: xsd:string']'''
        return self._client.service.GetErrorInfoSummaries(locale)

    def GetKeyboardLayout(self, locale):
        '''['locale: xsd:string']'''
        return self._client.service.GetKeyboardLayout(locale)

    def GetLocales(self):
        ''''''
        return self._client.service.GetLocales()

    def GetLocalizations(self, locale):
        '''['locale: xsd:string']'''
        return self._client.service.GetLocalizations(locale)

    def SaveUserComment(self, identifier, comment):
        '''['identifier: xsd:string', 'comment: xsd:string']'''
        return self._client.service.SaveUserComment(identifier, comment)


