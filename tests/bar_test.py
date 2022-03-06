import unittest
from src.bar import Bar 
from src.guest import Guest
from src.drink import Drink
from src.snack import Snack
from src.room import Room 

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar(300)

        self.guest = Guest("Jennifer", 16, 5.50, 0, 10, "Another Day", 2, 25)
        self.guest_2 = Guest("Lucy", 25, 28.50, 5, 7, "Wouldn't It Be Nice", 0, 5) 

        self.drink = Drink("pineapple margarita", 7, 5)
        self.drink_2 = Drink("spiced gold rum", 6, 5)
        self.drink_3 = Drink("red wine", 5, 3.5)

        self.snack = Snack("pinapple fritters", 4, 2, 6)
        self.snack_2 = Snack("mixed nuts", 2.50, 1, 2)
        self.snack_3 = Snack("sweet potato fries", 5, 3, 7)

        self.room = Room(2, 2, 5)

    def test_bar_has_till(self):
        self.assertEqual(300, self.bar.till)

    def test_check_customer_is_18(self):
        self.bar.check_customer_is_18(self.guest)
        self.assertEqual(False, self.bar.check_customer_is_18(self.guest))

    def test_serve_customer__till_increases(self):
        self.bar.serve_customer(self.guest_2, self.drink)
        self.assertEqual(307, self.bar.till)
    
    def test_add_drink_to_stock(self):
        self.bar.add_drink_to_stock(self.drink, 30)
        self.bar.add_drink_to_stock(self.drink_2, 30) 
        self.bar.add_drink_to_stock(self.drink_3, 70)
        self.assertEqual({"pineapple margarita": 30, "spiced gold rum": 30, "red wine": 70}, self.bar.drinks_stock)
    
    def test_add_snack_to_stock(self):
        self.bar.add_snack_to_stock(self.snack, 20)
        self.bar.add_snack_to_stock(self.snack_2, 60)
        self.bar.add_snack_to_stock(self.snack_3, 30)
        self.assertEqual({"pinapple fritters": 20, "mixed nuts": 60, "sweet potato fries": 30}, self.bar.snacks_stock)
    
    def test_add_item_to_room_tab(self):
        self.bar.add_item_to_room_tab(self.room, self.snack)
        self.bar.add_item_to_room_tab(self.room, self.drink)
        self.assertEqual(11, self.room.room_tab)
    
    




    


