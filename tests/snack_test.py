import unittest
from src.snack import Snack 

class TestSnack(unittest.TestCase):

    def setUp(self):
        self.snack = Snack("sweet potato fries", 5.00, 2, 4)
    
    def test_snack_has_name(self):
        self.assertEqual("sweet potato fries", self.snack.name)
                                                
    def test_snack_has_price(self):
        self.assertEqual(5.00, self.snack.price) 
            
    def test_snack_sobering_effect(self):
        self.assertEqual(2, self.snack.sobering_effect)     
    
    def test_snack_satiety_effect(self):
        self.assertEqual(4, self.snack.satiety_effect)    