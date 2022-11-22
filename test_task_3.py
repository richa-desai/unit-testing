''' This file is for Python Unit Test Project Problem 3'''
import unittest
from task_3 import get_match_ids_of_a_year, calculate

class TestTask1(unittest.TestCase):
    ''' Test Class for Task 3 '''
    match_ids_of_2016 = ['580', '581']
    extra_runs_in_2016 = {'Sunrisers Hyderabad': 1, 'Royal Challengers Bangalore': 5,
                          'Mumbai Indians': 1, 'Kolkata Knight Riders': 1}

    def test_get_match_ids_of_a_year(self):
        ''' Test method for Task 3 get_match_ids_of_a_year method '''
        result = get_match_ids_of_a_year('2016', "mock_matches.csv")
        self.assertCountEqual(result, self.match_ids_of_2016)

    def test_calculate(self):
        ''' Test method for Task 3 calculate method '''
        result = calculate('mock_deliveries.csv')
        self.assertDictEqual(result, self.extra_runs_in_2016)

if __name__ == '__main__':
    unittest.main()
