import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Du Hast", "Rammstein")
        self.guest_1 = Guest("Jim", 1000, Song("Running Up That Hill", "Kate Bush"))
        self.guest_2 = Guest("Joe", 100, Song("Hounds of Love", "Kate Bush"))
        self.guest_3 = Guest("Jamie", 60, self.song_1)
        self.guest_4 = Guest("Joey", 1000, self.song_1)
        self.room_1 = Room([Guest("Jeff", 500, self.song_1), Guest("Jenny", 90, self.song_1)], 5, 100)
        self.room_2 = Room([self.guest_1, self.guest_2], 2, 50)

    def test_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(3, len(self.room_1.guests))
        self.assertEqual(100, self.room_1.tab)

    def test_dont_check_in_if_at_capacity(self):
        self.room_2.check_in_guest(self.guest_3)
        self.assertEqual(2, len(self.room_2.guests))

    def test_dont_check_in_if_guest_cant_afford(self):
        self.room_1.check_in_guest(self.guest_3)
        self.assertEqual(2, len(self.room_1.guests))

    def test_check_out_guest(self):
        self.room_1.check_out_guest(self.room_1.guests[0])
        self.assertEqual(1, len(self.room_1.guests))

    def test_check_room_has_capacity(self):
        self.assertEqual(5, self.room_1.capacity)

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

    def test_if_room_has_fave(self):
        self.room_1.songs = [Song("Running Up That Hill", "Kate Bush"), Song("Hounds of Love", "Kate Bush")]
        self.assertEqual("Yes! Love Running Up That Hill", self.room_1.check_in_guest(self.guest_1))

    def test_if_room_does_not_have_fave(self):
        self.room_1.songs = [Song("Running Up That Hill", "Kate Bush"), Song("Hounds of Love", "Kate Bush")]
        self.assertEqual("Boo. No Du Hast", self.room_1.check_in_guest(self.guest_4))