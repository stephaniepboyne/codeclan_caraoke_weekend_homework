import unittest
from src.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Wouldn't It Be Nice", "The Beach Boys")
    
    def test_song_has_name(self):
        self.assertEqual("Wouldn't It Be Nice", self.song.name)
    
    def test_song_has_artist(self):
        self.assertEqual("The Beach Boys", self.song.artist)
    
    


