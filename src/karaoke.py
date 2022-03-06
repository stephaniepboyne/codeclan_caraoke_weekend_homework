class Karaoke:

    def __init__(self, name, till, number_of_rooms, number_of_available_rooms):
        self.name = name
        self.till = till
        self.number_of_rooms = number_of_rooms
        self.number_of_available_rooms = number_of_available_rooms
    
    def room_big_enough(self, guests, room):
        return len(guests) <= room.capacity 

    def check_in_guest(self, guests, room):
        if (self.number_of_available_rooms >= 1) and (self.room_big_enough(guests, room)): 
            self.number_of_available_rooms -= 1 
            self.till += room.entry_fee 
            room.room_status = "occupied"
    
    def add_song_to_room_playlist(self, songs, room):
        for song in songs:
            room.play_list[song.name] = song.artist 
    
    def check_out_guest(self, room):
        self.number_of_available_rooms += 1
        room.room_status = "unoccupied"