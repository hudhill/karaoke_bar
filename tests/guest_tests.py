import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Joe")

    def test_guest_has_name(self):
        self.assertEqual("Joe", self.guest.name)
