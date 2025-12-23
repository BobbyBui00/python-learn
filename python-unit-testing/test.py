import unittest
import main


class TestMain(unittest.TestCase):

    def setUp(self):
        ## Run it at the begining of each test case
        print('About to test a function')

    def test_do_stuff(self):
        """Positive scenario"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff_2(self):
        test_param = 'ADSFADSF'
        result = main.do_stuff(test_param)
        # self.assertEqual(isinstance(result, ValueError))
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff_3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_stuff_4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        ## Run it at the end of each test case. Usually for cleanup
        print('Clean up')


if __name__ == '__main__':
    unittest.main()
