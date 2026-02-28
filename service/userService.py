from utiltiy.hashUtility import HashUtility
from repository.userRepository import UserRepository
from flask import session


class UserService:

    AUSBILDUNGSBETRIEB = 1
    ORGANISATIONSTEAM = 2
    LEHRER = 3

    def __init__(self):
        self.userRepository = UserRepository()
        pass

    def userExist(self, email: str, password: str = None):
        if password is not None:
            if self.userRepository.getByPasswordAndEmail(email, password):
                return self.userRepository.getByPasswordAndEmail(email, password)

            return False

        if self.userRepository.getByEmail(email):
            return True

        return False

    def registerUser(self, company: str, email: str, password: str):
        if self.userExist(email):
            return False

        self.userRepository.insert(
            [
                {
                    'company': company,
                    'email': email,
                    'password_hash': HashUtility.hash(password),
                    'role': 1,
                    'donation': 0
                }
            ]
        )
        return True
        
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

    def getUserEmail(self):
        user = self.getUser()
        if user != []:
            userEmail = user[0]['email']
            return userEmail


    def getRoleOfUser(self):
        user = self.getUser()
        if (user != []):
            user_role = user[0]['role']
            return user_role
        return []
    
    def getUserUid(self):
        if ('uid' in session):
            return session['uid']
        return 0
    
    def logoutUser(self):
        if 'uid' in session:
            session.pop('uid')



