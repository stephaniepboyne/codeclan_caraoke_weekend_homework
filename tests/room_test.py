import unittest
from src.room import Room 

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(5, 8, 8, "unoccupied")
    
    def test_room_has_number(self):
        self.assertEqual(5, self.room.room_number)
                        
    def test_room_has_capacity(self):
        self.assertEqual(8, self.room.capacity) 
    
    def test_room_has_entry_fee(self):
        self.assertEqual(8, self.room.entry_fee)