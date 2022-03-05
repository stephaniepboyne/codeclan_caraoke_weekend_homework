class Bar:

    def __init__(self, till):
        self.till = till
        self.drinks_menu = []
        self.snacks_menu = []
        self.drinks_stock = {}
        self.snacks_stock = {}
    
    def check_customer_is_18(self, guest):
        return guest.age >= 18
    
    def serve_customer(self, guest, drink):
        if self.check_customer_is_18(guest):
            self.till += drink.price
            for 
            self.drinks_stock
