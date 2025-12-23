from unittest import mock, TestCase
import unittest
import random
import main


class TestMain(TestCase):

    @mock.patch('main.input', create=True)
    def setUp(self, mocked_input):
        self.computer_guess = random.randint(1, 2)
        self.user_guess = int(input('Enter a random number from 1 to 10: '))
        print(f'User guess {self.user_guess} - Computer guess {self.computer_guess}')

    def test_function(self):
        result = main.compare(computer_guess=self.computer_guess, user_guess=self.user_guess)
        self.assertEqual(result, True if self.user_guess == self.computer_guess else None)


if __name__ == '__main__':
    unittest.main()
