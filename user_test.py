import unittest
from user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user_account = User('facebook', 'benoba', 'eggs')

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.user_account.account, 'facebook')
        self.assertEqual(self.user_account.user_name, 'benoba')
        self.assertEqual(self.user_account.password, 'eggs')


if __name__ == '__main__':
    unittest.main()
