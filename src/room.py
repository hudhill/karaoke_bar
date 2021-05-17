class Room:

    def __init__(self, guests, capacity, rate):
        self.guests = guests
        self.songs = []
        self.capacity = capacity
        self.rate = rate
        self.tab = 0

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity and guest.can_pay_rate(self):
            self.guests.append(guest)
            self.tab += self.rate
            song_titles = [song.title for song in self.songs]
            if guest.fave_song.title in song_titles:
                return f"Yes! Love {guest.fave_song.title}"
            else:
                return f"Boo. No {guest.fave_song.title}"

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)
