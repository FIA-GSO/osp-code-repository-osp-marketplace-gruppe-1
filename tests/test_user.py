import unittest
from repository.userRepository import UserRepository
from service.userService import UserService

class test_user(unittest.TestCase):

    userRepository = UserRepository()
    userService = UserService()

    def test_add_user(self):
        self.userService.registerUser('testCompany', 'testEmail@example.de', 'test')
        result = self.userService.userExist('testEmail@example.de')
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()
