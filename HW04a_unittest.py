from HW04a_function import git_rep
import unittest

#  git_rep function is being tested. This script has 3 testcases.

class test_rep(unittest.TestCase):

    def testcase1(self): #  Here assertEqual is being used and the git_rep function returns true when it is able to connect with git user id rajguru7337 and then display repositories and number of commits
        self.assertEqual(git_rep('rajguru7337'), True, 'True')

    def testcase2(self):#  Here asserNotEqual is being used and the git_rep function returns false as it is not able to connect with rajgurug
        self.assertNotEqual(git_rep('rajgurug'), False, 'False')

    def testcase3(self):#  Here asserNotEqual is being used and the git_rep function returns false as it is not able to connect with rajguru
        self.assertNotEqual(git_rep('rajguru'), False, 'False')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()






