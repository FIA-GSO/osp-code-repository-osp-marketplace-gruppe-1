import unittest
from repository.userRepository import UserRepository
from service.userService import UserService


class TestUserRepository(unittest.TestCase):

    userRepository = UserRepository()
    userService = UserService()

    def TestAddUser(self):
        self.userService.registerUser('testCompany', 'testEmail@example.de', 'test')
        result = self.userService.userExist('testEmail@example.de', 'test')
        self.assertEqual(result, True)

        self.userService.loginUser('testEmail@example.de', 'test')
        currentUser = self.userService.getUser()

        self.assertEqual(currentUser['email'], 'testEmail@example.de')



if __name__ == "__main__":
    unittest.main()
