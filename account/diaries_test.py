import unittest
from diaries import Diaries
from diary import Diary


class Diaries_test(unittest.TestCase):
    def setUp(self):
        self.diaries = Diaries()

    def test_can_add_diary(self):
        self.diaries.add_diary("james", "1234")
        self.diaries.find_by_username("james")
        self.assertEqual("james", self.diaries.find_by_username("james").get_diary_username())
        self.diaries.add_diary("mike", "2367")
        self.diaries.find_by_username("mike")
        self.assertEqual("mike", self.diaries.find_by_username("mike").get_diary_username())


    def test_i_can_find_diary(self):
        self.diaries.add_diary("mike", "2367")
        self.diaries.find_by_username("mike")
        self.assertEqual("mike", self.diaries.find_by_username("mike").get_diary_username())


    def test_i_can_delete_from_diary(self):
        self.diaries.add_diary("akpabio", "1234")
        self.diaries.find_by_username("akpabio")
        self.assertEqual("akpabio", self.diaries.find_by_username("akpabio").get_diary_username())
        self.diaries.add_diary("mike", "2367")
        self.diaries.find_by_username("mike")
        self.assertEqual("mike", self.diaries.find_by_username("mike").get_diary_username())
        self.diaries.i_can_delete("akpabio", "1234")
        # self.assertIsNone(self.diaries.find_by_username("akpabio"))
        with self.assertRaises(AttributeError):
            self.diaries.find_by_username("akpabio")
        self.diaries.i_can_delete("mike", "2367")
        with self.assertRaises(AttributeError):
            self.diaries.find_by_username("mike")
        # self.assertIsNone(self.diaries.find_by_username("mike"))
