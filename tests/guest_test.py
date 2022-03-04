import unittest
from src.guest import Guest 
from src.drink import Drink 
from src.snack import Snack 
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Lucy", 25, 28.50, 5, 7, "Wouldn't It Be Nice", 0, 5)  
        self.guest_2 = Guest("Henry", 36, 38.60, 65, 0, "Could You Be Loved", 15, 28)
        self.guest_3 = Guest("Ula", 37, 5.20, 45, 0, "Over the Rainbow", 10, 50)

        self.drink = Drink("pina colada", 7, 5)

        self.snack = Snack("mixed nuts", 2.50, 1, 2)

        self.room = Room(5, 4, 4)

        self.song = Song("Could You Be Loved", "Bob Marley")
        self.song_2 = Song("Wouldn't It Be Nice", "The Beach Boys")
        self.song_3 = Song("Over the Rainbow", "Israel Kamakawiwo'ole")
        self.song_4 = Song("Is This Love", "Bob Marley")
        self.song_5 = Song("Do You Realize??", "The Flaming Lips")


    def test_guest_has_name(self):
        self.assertEqual("Lucy", self.guest.name)   

    def test_guest_has_age(self):
        self.assertEqual(25, self.guest.age)       

    def test_guest_wallet(self):
        self.assertEqual(28.50, self.guest.wallet)

    def test_guest_drunkenness(self):
        self.assertEqual(5, self.guest.drunkenness)   
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Wouldn't It Be Nice", self.guest.favourite_song)
    
    def test_guest_has_singing_ability(self):
        self.assertEqual(7, self.guest.singing_ability)

    def test_guest_has_munchies_level(self):
        self.assertEqual(0, self.guest.munchies_level)
    
    def test_sufficient_funds(self):
        result = self.guest.sufficient_funds(self.drink)
        self.assertEqual(True, result)

    def test_guest_can_buy_drink(self):
        result = self.guest.guest_can_buy_drink()
        self.assertEqual(True, result)
    
    def test_buy_drink__wallet_decreases(self):
        self.guest.buy_drink(self.drink)
        result = self.guest.wallet
        self.assertEqual(21.50, result)
    
    def test_buy_drink__drunkenness_increases(self):
        self.guest.buy_drink(self.drink)
        result = self.guest.drunkenness
        self.assertEqual(10, result)
    
    def test_buy_drink__singing_ability_decreases(self):
        self.guest_2.buy_drink(self.drink)
        result = self.guest_2.singing_ability
        self.assertEqual(0, result)
    
    def test_buy_drink__munchies_level_increases(self):
        self.guest.buy_drink(self.drink)
        result = self.guest.munchies_level
        self.assertEqual(2.5, result)
    
    def test_buy_drink__happy_mood_changes(self):
        self.guest_2.buy_drink(self.drink)
        result = self.guest_2.happy_mood 
        self.assertEqual(25.5, result)
    
    def test_buy_snack__munchies_level_decreases(self):
        self.guest.buy_snack(self.snack)
        result = self.guest.munchies_level
        self.assertEqual(0, result)
    
    def test_buy_snack__drunkenness_decreases(self):
        self.guest.buy_snack(self.snack)
        result = self.guest.drunkenness
        self.assertEqual(4, result)

    def test_buy_snack__wallet_decreases(self):
        self.guest.buy_snack(self.snack)
        result = self.guest.wallet 
        self.assertEqual(26, result)

    def test_check_into_room(self):
        self.guest.check_into_room(self.room)
        result = self.guest.wallet 
        self.assertEqual(24.50, result)
    
    def test_sing_favourite_song__happy_mood_increases(self):
        self.guest_2.sing_song(self.song)
        result = self.guest_2.happy_mood
        self.assertEqual(36, result)
    
    def test_sing_song__happy_mood_increases(self):
        self.guest.sing_song(self.song)
        result = self.guest.happy_mood
        self.assertEqual(9, result)
    
    def test_sing_song__happiest(self):
        self.guest_3.sing_song(self.song)
        result = self.guest_3.happy_mood
        self.assertEqual(50, result)
    
    def test_sees_favourite_song_in_playlist(self):
        self.room.play_list = [self.song, self.song_2, self.song_3, self.song_4, self.song_5]
        self.assertEqual("Woohoo!", self.guest_3.sees_favourite_song_in_playlist(self.room))
    
    def test_sees_favourite_song_in_playlist_happy_mood_increases(self):
        self.room.play_list = [self.song, self.song_2, self.song_3, self.song_4, self.song_5]
        self.guest.sees_favourite_song_in_playlist(self.room)
        self.assertEqual(9, self.guest.happy_mood)
        
