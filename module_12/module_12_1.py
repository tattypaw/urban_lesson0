import unittest

import runner
from unittest import TestCase

class RunnerTest(TestCase):
    def test_walk(self):
        runner1 = runner.Runner('Igor')
        for i in range(20):
            runner1.walk()
        self.assertEqual(runner1.distance, 100)

    def test_run(self):
        runner1 = runner.Runner('Igor')
        for i in range(15):
            runner1.run()
        self.assertEqual(runner1.distance, 150)

    def test_challenge(self):
        runner1 = runner.Runner('Igor')
        runner2 = runner.Runner('Peter')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
    unittest.main()

