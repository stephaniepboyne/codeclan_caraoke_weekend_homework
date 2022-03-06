class Bar:

    def __init__(self, till):
        self.till = till
        self.drinks_stock = {}
        self.snacks_stock = {}
    
    def check_customer_is_18(self, guest):
        return guest.age >= 18
    
    def serve_customer(self, guest, drink):
        if self.check_customer_is_18(guest):
            self.till += drink.price
    
    def add_drink_to_stock(self, drink, number):
        self.drinks_stock[drink.name] = number

    def add_snack_to_stock(self, snack, number):
        self.snacks_stock[snack.name] = number 
    
    def add_item_to_room_tab(self, room, item):
        room.room_tab += item.price 