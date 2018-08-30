from fastems import services

class NcLibraryService(services.FastemsService):
    def __init__(self):
        super().__init__('NcLibraryService')

    def AddNcProgram(self, requestor, request):
        '''['requestor: ns3:RequestorDto', 'request: ns4:AddNcProgramRequestDto']'''
        return self._client.service.AddNcProgram(requestor, request)

    def AttachFile(self, requestor, programId, filename, fileSize):
        '''['requestor: ns3:RequestorDto', 'programId: ns2:guid', 'filename: xsd:string', 'fileSize: xsd:long']'''
        return self._client.service.AttachFile(requestor, programId, filename, fileSize)

    def CreateNcFolder(self, requestor, ncGroupId, path):
        '''['requestor: ns3:RequestorDto', 'ncGroupId: ns4:NcGroupIdentityDto', 'path: xsd:string']'''
        return self._client.service.CreateNcFolder(requestor, ncGroupId, path)

    def DeleteImportFiles(self, requestor, paths):
        '''['requestor: ns3:RequestorDto', 'paths: ns7:ArrayOfstring']'''
        return self._client.service.DeleteImportFiles(requestor, paths)

    def GetNcProgram(self, id):
        '''['id: ns2:guid']'''
        return self._client.service.GetNcProgram(id)

    def GetSubprogramUsages(self, subprogramId):
        '''['subprogramId: ns2:guid']'''
        return self._client.service.GetSubprogramUsages(subprogramId)

    def GetToolUsingNcProgramsIds(self, toolId):
        '''['toolId: ns8:ToolBaseDataIdentityDto']'''
        return self._client.service.GetToolUsingNcProgramsIds(toolId)

    def ImportFiles(self, requestor, source, files):
        '''['requestor: ns3:RequestorDto', 'source: ns4:NcImportSourceDto', 'files: ns4:ArrayOfNcImportFileDto']'''
        return self._client.service.ImportFiles(requestor, source, files)

    def MoveNcProgram(self, requestor, programId, targetFolderId):
        '''['requestor: ns3:RequestorDto', 'programId: ns2:guid', 'targetFolderId: ns2:guid']'''
        return self._client.service.MoveNcProgram(requestor, programId, targetFolderId)

    def RemoveNcFolder(self, requestor, id):
        '''['requestor: ns3:RequestorDto', 'id: ns2:guid']'''
        return self._client.service.RemoveNcFolder(requestor, id)

    def RemoveNcProgram(self, requestor, id):
        '''['requestor: ns3:RequestorDto', 'id: ns2:guid']'''
        return self._client.service.RemoveNcProgram(requestor, id)

    def SaveImportSettings(self, requestor, settings):
        '''['requestor: ns3:RequestorDto', 'settings: ns4:NcImportSettingsDto']'''
        return self._client.service.SaveImportSettings(requestor, settings)

    def UpdateNcProgram(self, requestor, request):
        '''['requestor: ns3:RequestorDto', 'request: ns4:UpdateNcProgramRequestDto']'''
        return self._client.service.UpdateNcProgram(requestor, request)

    def UpdateNcProgramDuration(self, requestor, request):
        '''['requestor: ns3:RequestorDto', 'request: ns4:UpdateNcProgramDurationRequestDto']'''
        return self._client.service.UpdateNcProgramDuration(requestor, request)

    def UseMeasuredToolUsages(self, requestor, programId):
        '''['requestor: ns3:RequestorDto', 'programId: ns2:guid']'''
        return self._client.service.UseMeasuredToolUsages(requestor, programId)


