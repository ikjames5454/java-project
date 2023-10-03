import unittest
from diary import Diary
from entry import Entry


class Diary_test(unittest.TestCase):

    def setUp(self):
        self.diary = Diary("james", "2345")

    def test_can_lock_diary(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)

    def test_unlock_diary(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.unlock_diary("2345")
        self.assertFalse(self.diary.isLock)

    def test_is_lock(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.unlock_diary("2345")
        self.assertFalse(self.diary.isLock)
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)

    def test_i_can_create_entry(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.unlock_diary("2345")
        self.assertFalse(self.diary.isLock)
        self.diary.entry_creation("myDearDairy", "you are wonderfully made")
        self.diary.can_find_entry(1)
        self.assertEqual("myDearDairy", self.diary.can_find_entry(1).get_title())
        self.diary.entry_creation( "myDairy", "you are wonderfully and beautifully made")
        self.diary.can_find_entry(2)
        self.assertEqual("myDairy"   "you are wonderfully and beautifully made",
                         self.diary.can_find_entry(2).get_entry())

    def test_i_can_find_entry_by_id(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.unlock_diary("2345")
        self.assertFalse(self.diary.isLock)
        self.diary.entry_creation("myDearDairy", "you are wonderfully made")
        self.assertEqual("myDearDairy", self.diary.can_find_entry(1).get_title())

    def test_i_can_delete_entry_by_id(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.unlock_diary("2345")
        self.assertFalse(self.diary.isLock)
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.entry_creation("myDearDairy", "you are wonderfully made")
        self.assertEqual("myDearDairy", self.diary.can_find_entry(1).get_title())
        self.diary.entry_deletion(1)
        # with self.assertRaises(AttributeError):
        #     self.diary.can_find_entry(1)
        self.assertIsNone(self.diary.can_find_entry(1))

    def test_i_can_update_entry_(self):
        self.diary.lock_diary()
        self.assertTrue(self.diary.isLock)
        self.diary.unlock_diary("2345")
        self.assertFalse(self.diary.isLock)
        self.diary.entry_creation("myDearDairy", "you are wonderfully made")
        self.diary.update_entry(1, "myDairy", "you are wonderful")
        self.assertEqual(Entry(1, "myDairy", "you are wonderful").get_entry(), self.diary.can_find_entry(1).get_entry())
        self.diary.entry_creation("myMY", "you are wonderful")
        self.diary.update_entry(2, "JOURNAL OF GOSSIP", "wetin dey sub for class")
        self.assertEqual(Entry(2, "JOURNAL OF GOSSIP", "wetin dey sub for class").get_entry(), self.diary.can_find_entry(2).get_entry())
