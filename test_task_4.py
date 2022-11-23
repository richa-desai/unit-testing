''' This file is for Python Unit Test Project Problem 4'''
import unittest
from task_4 import calculate, transform

class TestTask1(unittest.TestCase):
    ''' Test Class for Task 4 '''
    bowlerwise_runs_2015 = {'UT Yadav': {'Bowler runs': 4, 'Ball count': 6},
                            'M Morkel': {'Bowler runs': 5, 'Ball count': 6},
                            'SL Malinga': {'Bowler runs': 3, 'Ball count': 7},
                            'R Vinay Kumar': {'Bowler runs': 2, 'Ball count': 6},
                            'JA Morkel': {'Bowler runs': 16, 'Ball count': 6},
                            'NM Coulter-Nile': {'Bowler runs': 10, 'Ball count': 7},
                            'A Nehra': {'Bowler runs': 4, 'Ball count': 6},
                            'MM Sharma': {'Bowler runs': 9, 'Ball count': 6}}
    top_bowlers_of_2015 = {'R Vinay Kumar': 0.3333333333333333,
                           'SL Malinga': 0.42857142857142855,
                           'UT Yadav': 0.6666666666666666,
                           'A Nehra': 0.6666666666666666,
                           'M Morkel': 0.8333333333333334,
                           'NM Coulter-Nile': 1.4285714285714286,
                           'MM Sharma': 1.5,
                           'JA Morkel': 2.6666666666666665}
    top_4_bowlers_of_2015 = {'R Vinay Kumar': 0.3333333333333333,
                             'SL Malinga': 0.42857142857142855,
                             'UT Yadav': 0.6666666666666666,
                             'A Nehra': 0.6666666666666666}
    top_3_bowlers_of_2015 = {'R Vinay Kumar': 0.3333333333333333,
                             'SL Malinga': 0.42857142857142855,
                             'UT Yadav': 0.6666666666666666,
                             'A Nehra': 0.6666666666666666}

    def test_calculate(self):
        ''' Test method for Task 4 calculate method '''
        result = calculate('mock_deliveries.csv')
        self.assertDictEqual(result, self.bowlerwise_runs_2015)

    def test_transform(self):
        ''' Test method for Task 4 transform method '''
        result = transform(self.bowlerwise_runs_2015, 3)
        self.assertDictEqual(result, self.top_3_bowlers_of_2015)

if __name__ == '__main__':
    unittest.main()
