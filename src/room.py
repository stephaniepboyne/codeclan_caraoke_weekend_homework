class Room:
    
    def __init__(self, room_number, capacity, entry_fee):
        self.room_number = room_number
        self.capacity = capacity
        self.play_list = {}
        self.entry_fee = entry_fee
        self.room_tab = 0 
    
    