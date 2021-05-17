class Guest:

    def __init__(self, name, wallet, fave_song):
        self.name = name
        self.wallet = wallet
        self.fave_song = fave_song

    def can_pay_rate(self, room):
        if room.rate <= self.wallet:
            self.wallet -= room.rate
            return True
        else:
            return False