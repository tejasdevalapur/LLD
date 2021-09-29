

from services.User_Service_Interface import UserServiceInterface
from models.User import User


class UserService(UserServiceInterface):

    userDetails={}

    def addUser(self,id,name):
        user=User()
        user.setId(id)
        user.setName(name)

        self.__class__.userDetails[id]=user
        return user








