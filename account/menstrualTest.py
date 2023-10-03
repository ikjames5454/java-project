import unittest
from menstrual import Menstrual
from datetime import datetime


class MenstrualTest(unittest.TestCase):
    def setUp(self) -> None:
        self.menstrual = Menstrual()

    def test_that_menstrual_app_can_predict_next_period_date(self):
        actual = self.menstrual.check_next_flow_date("2023-10-12",28)
        expected = datetime.strptime("2023-11-10", "%Y-%m-%d")
        self.assertEqual(actual,expected)
        actuals = self.menstrual.check_next_flow_date("2023-11-17",28)
        expect = datetime.strptime("2023-12-16", "%Y-%m-%d")
        self.assertEqual(actuals,expect)


    def test_ThatMenstrualApp_CheckEndOfCircle(self):
        actual = self.menstrual.check_end_of_menstrual_cycle("2023-10-12",28)
        expected = datetime.strptime("2023-11-9", "%Y-%m-%d")
        self.assertEqual(actual, expected)
        actuals = self.menstrual.check_next_flow_date("2023-11-16", 28)
        expect = datetime.strptime("2023-12-15", "%Y-%m-%d")
        self.assertEqual(actuals, expect)

    def test_ThatMenstrualApp_CanPredictTheNextOvulationDate(self):
        actual = self.menstrual.ovulation_date("2023-10-12", 28)
        expected = datetime.strptime("2023-10-26", "%Y-%m-%d")
        self.assertEqual(actual, expected)
        actuals = self.menstrual.ovulation_date("2023-11-16", 28)
        expect = datetime.strptime("2023-11-30", "%Y-%m-%d")
        self.assertEqual(actuals, expect)

    def test_ThatMenstrualApp_CanPredictTheNextSafeDate(self):
        actual = self.menstrual.next_safe_date("2023-10-12", 28)
        expected = datetime.strptime("2023-11-2", "%Y-%m-%d")
        self.assertEqual(actual, expected)

