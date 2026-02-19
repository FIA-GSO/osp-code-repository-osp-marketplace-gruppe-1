from utiltiy.hashUtility import HashUtility
from repository.userRepository import UserRepository
from flask import session


class UserService:
    def __init__(self):
        self.userRepository = UserRepository()
        pass

    def userExist(self, email: str, password: str):
        if self.userRepository.getByPasswordAndEmail(email, password):
            return self.userRepository.getByPasswordAndEmail(email, password)
        else:
            return False
        
    def registerUser(self, email: str, company: str, role: int, donation: int, password: str):
        if (not self.userExist(email, password)):
            self.userRepository.insert(
            [
                {
                    'company': company,
                    'email': email,
                    'password_hash': HashUtility.hash(password),
                    'role': role,
                    'donation': donation
                }
            ]
    )
        
    def loginUser(self, email: str, password: str):
        if self.userExist(email, password):
            user = self.userExist(email, password)[0]
            session['uid'] = user['uid']
            return True
        return False

    def getUser(self):
        if ('uid' in session):
            return self.userRepository.getById(int(session['uid']))
        return []
    
    def logoutUser(self):
        if 'uid' in session:
            session.pop('uid')



