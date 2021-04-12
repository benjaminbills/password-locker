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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the contact list
        '''
        self.user_account.save_user_account()  # saving the new user
        self.assertEqual(len(User.user_account_list), 1)
    # setup and class creation up here

    def test_display_all_user_accounts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_user_accounts(), User.user_account_list)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.user_account.save_user_account()
        test_user = User("Test", "user", "user")  # new contact
        test_user.save_user_account()

        user_exists = User.account_exist("Test")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
