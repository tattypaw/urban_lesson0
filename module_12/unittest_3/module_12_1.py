import unittest
import runner
from unittest import TestCase

def frozen(func):
    def freez(atr):
        if atr.is_frozen == True:
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func
    return freez

class RunnerTest(TestCase):
    is_frozen = False

    @frozen
    def test_walk(self):
        runner1 = runner.Runner('Igor')
        for i in range(20):
            runner1.walk()
        self.assertEqual(runner1.distance, 100)

    @frozen
    def test_run(self):
        runner1 = runner.Runner('Igor')
        for i in range(15):
            runner1.run()
        self.assertEqual(runner1.distance, 150)

    @frozen
    def test_challenge(self):
        runner1 = runner.Runner('Igor')
        runner2 = runner.Runner('Peter')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()

