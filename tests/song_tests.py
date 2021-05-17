import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Du Hast", "Rammstein")

    def test_song_has_title(self):
        self.assertEqual("Du Hast", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Rammstein", self.song.artist)