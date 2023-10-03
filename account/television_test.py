import unittest
from television import Television


class that_i_have(unittest.TestCase):



    def test_turn_on(self):
        self.tv = Television()
        self.tv.turn_on_()
        self.assertTrue(self.tv.on)


    def test_turn_off(self):
        self.tv = Television()
        self.tv.turn_on_()
        self.tv.turn_off_()
        self.assertFalse(self.tv.on)

    def test_get_channel(self):
        self.tv = Television()
        self.tv.get_channel()
        self.assertEqual(self.tv.get_channel(), 0)


    def test_set_channel(self):
        self.tv = Television()
        self.tv.set_channel(60)
        self.assertEqual(self.tv.get_channel(), 60)


    def test_get_volume(self):
        self.tv = Television()
        self.tv.get_channel()
        self.assertEqual(self.tv.get_volume(), 0)

    def test_set_volume(self):
        self.tv = Television()
        self.tv.set_volume(40)
        self.assertEqual(self.tv.get_volume(), 40)


    def test_volume_can_go_up(self):
        self.tv = Television()
        self.tv.turn_on_()
        self.tv.set_volume(50)
        self.tv.volume_up()
        self.assertEqual(self.tv.get_volume(), 51)

    def test_volume_can_go_down(self):
        self.tv = Television()
        self.tv.turn_on_()
        self.tv.set_volume(45)
        self.tv.volume_down()
        self.assertEqual(self.tv.get_volume(), 44)

    def test_channel_can_go_up(self):
        self.tv = Television()
        self.tv.turn_on_()
        self.tv.set_channel(68)
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 69)

    def test_channel_can_go_down(self):
        self.tv = Television()
        self.tv.turn_on_()
        self.tv.set_channel(34)
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel(), 33)


