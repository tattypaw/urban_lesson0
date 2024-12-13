import logging
import unittest
import rt_with_exceptions
from unittest import TestCase

class RunnerTest(TestCase):

    def test_walk(self):
        try:
            runner1 = rt_with_exceptions.Runner('Igor', -5)
            for i in range(20):
                runner1.walk()
            self.assertEqual(runner1.distance, 100)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.error('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner1 = rt_with_exceptions.Runner(10, 10)
            for i in range(15):
                runner1.run()
            self.assertEqual(runner1.distance, 300)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.error('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = rt_with_exceptions.Runner('Igor')
        runner2 = rt_with_exceptions.Runner('Peter')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

