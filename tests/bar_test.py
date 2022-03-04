import unittest
from src.bar import Bar 

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar(300)
    
    def test_bar_has_till(self):
        self.assertEqual(300, self.bar.till)
    


