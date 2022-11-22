''' This file is for Python Unit Test Project Problem 1'''
import unittest
from task_1 import calculate

class TestTask1(unittest.TestCase):
    ''' Test Class for Task 1 '''
    yearwise_matches_played = {2015: 2, 2016: 2}

    def test_calculate(self):
        ''' Test method for Task 1 calculate method '''
        result = calculate('mock_matches.csv')
        self.assertDictEqual(result, self.yearwise_matches_played)

if __name__ == '__main__':
    unittest.main()
