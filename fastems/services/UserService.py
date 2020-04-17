from fastems import services

class UserService(services.FastemsService):
    def __init__(self):
        super().__init__('UserService')

    def Authenticate(self, applicationName, credentials):
        '''['applicationName: xsd:string', 'credentials: ns2:CredentialsDto']'''
        return self._client.service.Authenticate(applicationName, credentials)

    def AuthenticateDefault(self, application):
        '''['application: ns2:ApplicationTypeDto']'''
        return self._client.service.AuthenticateDefault(application)

    def ChangeUserPassword(self, changePassword):
        '''['changePassword: ns2:ChangePasswordDto']'''
        return self._client.service.ChangeUserPassword(changePassword)

    def CreateRole(self, requestor, role):
        '''['requestor: ns4:RequestorDto', 'role: ns2:RoleDto']'''
        return self._client.service.CreateRole(requestor, role)

    def CreateUser(self, requestor, user):
        '''['requestor: ns4:RequestorDto', 'user: ns2:UserDto']'''
        return self._client.service.CreateUser(requestor, user)

    def GetFeatures(self):
        ''''''
        return self._client.service.GetFeatures()

    def GetRoles(self):
        ''''''
        return self._client.service.GetRoles()

    def GetUsers(self):
        ''''''
        return self._client.service.GetUsers()

    def RemoveRole(self, requestor, role):
        '''['requestor: ns4:RequestorDto', 'role: ns2:RoleDto']'''
        return self._client.service.RemoveRole(requestor, role)

    def RemoveUser(self, requestor, user):
        '''['requestor: ns4:RequestorDto', 'user: ns2:UserDto']'''
        return self._client.service.RemoveUser(requestor, user)

    def UpdateRole(self, requestor, role):
        '''['requestor: ns4:RequestorDto', 'role: ns2:RoleDto']'''
        return self._client.service.UpdateRole(requestor, role)

    def UpdateUser(self, requestor, user):
        '''['requestor: ns4:RequestorDto', 'user: ns2:UserDto']'''
        return self._client.service.UpdateUser(requestor, user)


