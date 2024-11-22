class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.__status = False  # TV is off by default
        self.__muted = True  # Not muted by default
        self.__volume = self.min_volume  # Start at minimum volume
        self.__channel = self.min_channel

    def power(self):
        if self.__status == True:
            self.__status = False
        elif self.__status == False:
            self.__status = True

    def mute(self):
        # Toggle mute state
        self.__muted = not self.__muted
        if not self.__muted:  # If unmuted, reset volume to last value
            self.__volume = self.min_volume if self.__volume == 0 else self.__volume

    def channel_up(self):
        if self.__status == True:
            self.__channel += 1
            if self.__channel > self.max_channel:  # Instead of checking if equal
                self.__channel = Television.min_channel

    def channel_down(self):
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < self.min_channel:
                self.__channel = Television.max_channel

    def volume_up(self):
        if self.__muted:
            self.__muted = False  # Unmute if volume is adjusted
        self.__volume += 1
        if self.__volume > self.max_volume:
            self.__volume = Television.max_volume

    def volume_down(self):
        if self.__muted:
            self.__muted = False  # Unmute if volume is adjusted
        self.__volume -= 1
        if self.__volume < self.min_volume:
            self.__volume = Television.min_volume

    def __str__(self):
        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}")
      
