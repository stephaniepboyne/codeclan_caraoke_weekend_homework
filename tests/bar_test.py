import unittest
from src.bar import Bar 
from src.guest import Guest

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar(300)
        self.guest = Guest("Jennifer", 16, 5.50, 0, 10, "Another Day", 2, 25)
    
    def test_bar_has_till(self):
        self.assertEqual(300, self.bar.till)

    def test_check_customer_is_18(self):
        self.bar.check_customer_is_18(self.guest)
        self.assertEqual(False, self.bar.check_customer_is_18(self.guest))


    


