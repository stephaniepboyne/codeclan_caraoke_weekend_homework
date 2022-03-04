import unittest
from src.karaoke import Karaoke 

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("The OO CodeClan Caraoke", 200, 10, 10)
    
    def test_karaoke_has_name(self):
        self.assertEqual("The OO CodeClan Caraoke", self.karaoke.name)

    def test_karaoke_has_till(self):
        self.assertEqual(200, self.karaoke.till)
    
    def test_karaoke_number_of_rooms(self):
        self.assertEqual(10, self.karaoke.number_of_rooms)
    
    def test_number_of_available_rooms(self):
        self.assertEqual(10, self.karaoke.number_of_available_rooms)
    
    