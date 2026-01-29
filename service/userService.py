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
        
    def registerUser(self, firstname: str, lastname: str, email: str, company: str, role: int, donation: int, password: str):
        self.userRepository.insert(
        [
            {
                'company': company,
                'first_name': firstname,
                'last_name': lastname,
                'email': email,
                'password_hash': HashUtility.hash(password),
                'role': 1,
                'donation': 0
            }
        ]
    )




