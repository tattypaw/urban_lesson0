import unittest
import module_12_1
import module_12_2

runnerTest = unittest.TestSuite()
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runnerTest.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerTest)


