import unittest
from src.room import Room
from src.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Du Hast", "Rammstein")

    def song_has_title(self):
        self.assertEqual("")

    def song_has_artist(self):