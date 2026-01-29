from utiltiy.hashUtility import HashUtility
from repository.userRepository import UserRepository


class UserService:
    def __init__(self):
        self.userRepository = UserRepository()
        pass

    def userExist(self, email: str, password: str):
        if self.userRepository.getByPasswordAndEmail(email, password) != []:
            return True
        else:
            return False



