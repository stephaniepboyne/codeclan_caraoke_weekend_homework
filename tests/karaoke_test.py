import unittest
from src.karaoke import Karaoke 
from src.guest import Guest
from src.room import Room 

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("The OO CodeClan Caraoke", 200, 5, 5)
        
        self.guest = Guest("Lucy", 25, 28.50, 5, 7, "Wouldn't It Be Nice", 0, 5)
        self.guest_2 = Guest("Henry", 36, 38.60, 58, 0, "Could You Be Loved", 15, 45)
        self.guest_3 = Guest("Ula", 37, 5.20, 45, 0, "Over the Rainbow", 10, 50)

        self.room = Room(1, 4, 10)
        self.room_2 = Room(2, 2, 5)
        self.room_3 = Room(3, 2, 5)
        self.room_4 = Room (4, 6, 15)
        self.room_5 = Room (5, 8, 20)
    
    def test_karaoke_has_name(self):
        self.assertEqual("The OO CodeClan Caraoke", self.karaoke.name)

    def test_karaoke_has_till(self):
        self.assertEqual(200, self.karaoke.till)
    
    def test_karaoke_number_of_rooms(self):
        self.assertEqual(5, self.karaoke.number_of_rooms)
    
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

    
    