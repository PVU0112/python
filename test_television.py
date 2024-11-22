import unittest
from television import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        """Set up a Television instance before each test."""
        self.tv = Television()

    def test_initial_state(self):
        """Test the initial state of the television."""
        self.assertFalse(self.tv._Television__status) 
        self.assertEqual(self.tv._Television__channel, Television.min_channel)
        self.assertEqual(self.tv._Television__volume, Television.min_volume)
        self.assertFalse(self.tv._Television__muted)  

    def test_power(self):
        """Test turning the TV on and off."""
        self.tv.power()
        self.assertTrue(self.tv._Television__status)  
        self.tv.power()
        self.assertFalse(self.tv._Television__status)  

    def test_channel_up(self):
        """Test channel up functionality."""
        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, Television.min_channel + 1)
        self.tv._Television__channel = Television.max_channel
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, Television.min_channel)

    def test_channel_down(self):
        """Test channel down functionality."""
        self.tv.power()
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, Television.max_channel)
        self.tv._Television__channel = Television.min_channel
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, Television.max_channel)

    def test_volume_up(self):
        """Test volume up functionality."""
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, Television.min_volume + 1)
        # Test volume clamping
        self.tv._Television__volume = Television.max_volume
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, Television.max_volume)

    def test_volume_down(self):
        """Test volume down functionality."""
        self.tv.power()
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, Television.min_volume)
        # Test volume clamping
        self.tv._Television__volume = Television.min_volume
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, Television.min_volume)

    def test_mute(self):
        """Test mute functionality."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, 0)
        self.tv.mute()
        self.assertFalse(self.tv._Television__muted)

    def test_unmute_with_restore_volume(self):
        """Test unmute restores the previous volume."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.mute()  # Unmute
        self.assertEqual(self.tv._Television__volume, Television.min_volume + 1)

    def test_adjust_volume_unmutes(self):
        """Test adjusting volume unmutes the TV."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_up()  
        self.assertFalse(self.tv._Television__muted)

    def test_str(self):
        """Test the __str__ method for correct output."""
        self.tv.power()
        self.assertEqual(str(self.tv), "Power = True, Channel = 0, Volume = 0")


if __name__ == '__main__':
    unittest.main()
