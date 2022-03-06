import unittest
from src.karaoke import Karaoke 
from src.guest import Guest
from src.room import Room 
from src.song import Song

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("The OO CodeClan Caraoke", 200, 6, 5)
        
        self.guest = Guest("Lucy", 25, 28.50, 5, 7, "Wouldn't It Be Nice", 0, 5)
        self.guest_2 = Guest("Henry", 36, 38.60, 58, 0, "Could You Be Loved", 15, 45)
        self.guest_3 = Guest("Ula", 37, 5.20, 45, 0, "Over the Rainbow", 10, 50)

        self.room = Room(1, 4, 10, "unoccupied")
        self.room_2 = Room(2, 2, 5, "unoccupied")
        self.room_3 = Room(3, 2, 5, "unoccupied")
        self.room_4 = Room (4, 6, 15, "unoccupied")
        self.room_5 = Room (5, 8, 20, "unoccupied")

        self.song = Song("Could You Be Loved", "Bob Marley")
        self.song_2 = Song("Wouldn't It Be Nice", "The Beach Boys")
        self.song_3 = Song("Over the Rainbow", "Israel Kamakawiwo'ole")
        self.song_4 = Song("Is This Love", "Bob Marley")
        self.song_5 = Song("Do You Realize??", "The Flaming Lips")
    
    def test_karaoke_has_name(self):
        self.assertEqual("The OO CodeClan Caraoke", self.karaoke.name)

    def test_karaoke_has_till(self):
        self.assertEqual(200, self.karaoke.till)
    
    def test_karaoke_number_of_rooms(self):
        self.assertEqual(6, self.karaoke.number_of_rooms)
    
    def test_number_of_available_rooms(self):
        self.assertEqual(5, self.karaoke.number_of_available_rooms)
    
    def tests_room_big_enough(self):
        self.karaoke.room_big_enough([self.guest, self.guest_2, self.guest_3], self.room_2)
        self.assertEqual(False, self.karaoke.room_big_enough([self.guest, self.guest_2, self.guest_3], self.room_2))

    def test_check_customer_in__number_of_availavle_rooms_decreases(self):
        self.karaoke.check_in_guest([self.guest, self.guest_2, self.guest_3], self.room)
        self.assertEqual(4, self.karaoke.number_of_available_rooms)
    
    def test_check_customer_in__till_increases(self):
        self.karaoke.check_in_guest([self.guest, self.guest_2, self.guest_3], self.room)
        self.assertEqual(210, self.karaoke.till) 

    def test_add_song_to_room_playlist(self):
        self.karaoke.add_song_to_room_playlist([self.song, self.song_2, self.song_3, self.song_4, self.song_5], self.room) 
        self.assertEqual({
            "Could You Be Loved": "Bob Marley", 
            "Wouldn't It Be Nice": "The Beach Boys", 
            "Over the Rainbow": "Israel Kamakawiwo'ole",
            "Is This Love": "Bob Marley",
            "Do You Realize??": "The Flaming Lips"}, self.room. play_list)
        
    def test_check_customer_out__number_of_availavle_rooms_increases(self):
        self.karaoke.check_out_guest(self.room)
        self.assertEqual(6, self.karaoke.number_of_available_rooms)
    
    def test_check_customer_out__room_status_changes(self):
        self.room_6 = Room(1, 4, 10, "occupied")
        self.karaoke.check_out_guest(self.room_6)
        self.assertEqual("unoccupied", self.room_6.room_status)