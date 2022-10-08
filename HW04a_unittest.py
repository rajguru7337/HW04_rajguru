from HW04a_function import git_rep
import unittest


class test_rep(unittest.TestCase):

    def testcase1(self):
        self.assertEqual(git_rep('rajguru7337'), True, 'True')

    def testcase2(self):
        self.assertNotEqual(git_rep('rajgurug'), False, 'False')

    def testcase3(self):
        self.assertNotEqual(git_rep('rajguru'), False, 'False')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()






