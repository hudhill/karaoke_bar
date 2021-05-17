import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Jim", 1000, Song("Running Up That Hill", "Kate Bush"))
        self.guest_2 = Guest("Joe", 50, Song("Hounds of Love", "Kate Bush"))
        self.room_3 = Room([], 5, 100)

    def test_guest_has_name(self):
        self.assertEqual("Joe", self.guest_2.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest_2.wallet)

    def test_guest_can_pay_rate(self):
        self.assertEqual(True, self.guest_1.can_pay_rate(self.room_3))
        self.assertEqual(900, self.guest_1.wallet)

    def test_guest_cant_pay_rate(self):
        self.assertEqual(False, self.guest_2.can_pay_rate(self.room_3))
        self.assertEqual(50, self.guest_2.wallet)

    def test_guest_has_fave_song(self):
        self.assertEqual("Running Up That Hill", self.guest_1.fave_song.title)
