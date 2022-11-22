''' This file is for Python Unit Test Project Problem 2'''
import unittest
from task_2 import calculate, transform

class TestTask1(unittest.TestCase):
    ''' Test Class for Task 1 '''
    season_victory_details = {2015: {'Kolkata Knight Riders': 1, 'Chennai Super Kings': 1},
                               2016: {'Royal Challengers Bangalore': 1, 'Mumbai Indians': 1}}
    season_victory_counts = [[0, 1, 1, 0], [1, 0, 0, 1]]

    def test_calculate(self):
        ''' Test method for Task 2 calculate method '''
        result = calculate('mock_matches.csv')
        self.assertDictEqual(result, self.season_victory_details)

    def test_transform(self):
        ''' Test method for Task 2 transform method '''
        result = transform(self.season_victory_details)
        self.assertEqual(len(result), len(self.season_victory_counts))
        self.assertCountEqual(result[0], self.season_victory_counts[0])
        self.assertCountEqual(result[1], self.season_victory_counts[1])

if __name__ == '__main__':
    unittest.main()
