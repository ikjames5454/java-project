class Television:
    def __init__(self):
        self.on = False
        self.channel = 0
        self.volume = 0

    def turn_on_(self):
        self.on = True

    def turn_off_(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_volume(self):
        return self.volume

    def set_volume(self,volume):
        self.volume = volume


    def volume_up(self):
        self.volume += 1


    def volume_down(self):
        self.volume -= 1

    def channel_up(self):
        self.channel += 1


    def channel_down(self):
        self.channel -= 1

