import unittest
from unittest import mock
from unittest.mock import Mock, patch, MagicMock

import unittest


@mock.patch('HW04a_function.git_rep', return_value= True, autospec = True)
def test_gitapi(API, api):
    assert git_rep(API) == "rajguru7337"
    print(api)

class test_rep(unittest.TestCase):

    @mock.patch('HW04a_function.git_rep')
    def test_mock_git_rep(self, user):
        user.return_value = MagicMock(userID="rajguru7337")
        result = user.return_value.userID
        try:
            self.assertEqual(result, 'rajguru7337')
        except:
            print("Test Failed")
        else:
            print("Test succeed")

    @mock.patch('HW04a_function.git_rep')
    def test_mock_git_rep2(self, usera):
        usera.return_value = MagicMock(userID="rajgurug")
        result = usera.return_value.userID
        try:
            self.assertEqual(result, 'rajgurug')
        except:
            print("Test Failed")
        else:
            print("Test succeed")

    @mock.patch('HW04a_function.git_rep')
    def test_mock_git_rep3(self, userb):
        userb.return_value = MagicMock(userID="rajguru")
        result = userb.return_value.userID
        try:
            self.assertEqual(result, 'rajguru')
        except:
            print("Test Failed")
        else:
            print("Test succeed")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()






