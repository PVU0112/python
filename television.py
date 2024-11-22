class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self):
        '''Initializes the televison

        '''
        self.__status = False  # TV is off by default
        self.__muted = False  # Not muted by default
        self.__volume = self.min_volume  # Start at minimum volume
        self.__channel = self.min_channel

    def power(self):
        '''Turns the tv on and off

        '''
        if self.__status == True:
            self.__status = False
        elif self.__status == False:
            self.__status = True

    def mute(self):
        '''Mutes the Volume while also keep tracking of the previous value incase it changes

        '''
        if self.__status:  # Ensure TV is on
            if self.__muted:  # If already muted, unmute and restore volume
                self.__muted = False
                self.__volume = self.previous_volume
            else:  # If not muted, store current volume and mute
                self.__muted = True
                self.previous_volume = self.__volume  # Save current volume
                self.__volume = 0  # Set volume to 0

    def volume_up(self):
        '''Increases the volume and stays at max if it goes beyond the max
        '''
        if self.__status:  # Ensure TV is on
            if self.__muted:
                self.__muted = False
                self.__volume = self.previous_volume
            self.__volume += 1
            if self.__volume > self.max_volume:  # Clamp to max volume
                self.__volume = self.max_volume

    def volume_down(self):
        '''decrease the volume and stays at min if it goes below the min
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.previous_volume
            self.__volume -= 1
            if self.__volume < self.min_volume:
                self.__volume = self.min_volume

    def channel_up(self):
        '''increase the channel and goes to min if it goes above the max
        '''
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.max_channel:
                self.__channel = Television.min_channel

    def channel_down(self):
        '''decrease the channel and goes to ax if it goes below the min
        '''
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.min_channel:
                self.__channel = Television.max_channel



    def __str__(self):
        '''Return Statement with values of the television
        
        '''
        return (f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}")
      
