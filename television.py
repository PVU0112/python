class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        self.__status = False         # TV is off by default
        self.__muted = False          # Not muted by default
        self.__volume = self.min_volume  # Start at minimum volume
        self.__channel = self.min_channel 
    def power(self):
        if self.__status == True:
            self.__status = False
        elif self.__status == False:
            self.__status = True
    def mute(self):
        if self.__muted == True:
            self.__muted = False
        elif self.__muted == False:
            self.__muted = True
    def channel_up(self):
       self.__channel += 1 
       if self.__channel == max_channel:
        self.__channel = min_channel
    def channel_down(self):   
       self.__channel -= 1 
       if self.__channel == min_channel:
         self.__channel = max_channel
    def volume_up(self):
      self.__muted == True:
       self.__volume += 1 
       if self.__volume == max_volume:
        self.__volume = min_volume
    def volume_down(self):
      self.__muted == True:
       self.__volume -= 1 
       if self.__volume == min_volume:
        self.__volume = max_volume
    def __str__(self):
        return (f'Power = [self.__status], Channel = [self.channel], Volume = [self.volume]')
      
