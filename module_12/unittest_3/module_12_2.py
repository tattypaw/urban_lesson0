from runner_and_tournament import Runner, Tournament
import unittest
from module_12_1 import frozen

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Usane', 10)
        self.runner2 = Runner('Andrew', 9)
        self.runner3 = Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for value in cls.all_results.values():
            print(f'{value}')
            '''i=0
            print('{', end='')
            for k, v in value.items():
                if i == len(value)-1:
                    print(f'{k}: {v}', end = '')
                    print('}')
                else:
                    print(f'{k}: {v}', end = ', ')
                i +=1'''

    @frozen
    def test_Usane_Nick(self):
        tour = Tournament(90, self.runner1, self.runner3)
        results = tour.start()
        self.assertTrue(results[max(results.keys())] == 'Nick')
        self.all_results[len(self.all_results)] = results

    @frozen
    def test_Andrew_Nick(self):
        tour = Tournament(90, self.runner2, self.runner3)
        results = tour.start()
        self.assertTrue(results[max(results.keys())] == 'Nick')
        self.all_results[len(self.all_results)] = results

    @frozen
    def test_All(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tour.start()
        self.assertTrue(results[max(results.keys())] == 'Nick')
        self.all_results[len(self.all_results)] = results

if __name__ == "__main__":
    unittest.main()