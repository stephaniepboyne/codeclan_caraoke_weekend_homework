class Guest:
    
    def __init__(self, name, age, wallet, drunkenness, singing_ability, favourite_song, munchies_level, happy_mood):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkenness = drunkenness
        self.singing_ability = singing_ability
        self.favourite_song = favourite_song
        self.munchies_level = munchies_level
        self.happy_mood = happy_mood
    
    def guest_can_buy_drink(self):
        return self.age >= 18

    def sufficient_funds(self, item):
        return self.wallet >= item.price

    def buy_drink(self, drink):
        if self.guest_can_buy_drink and self.sufficient_funds(drink):
            self.wallet -= drink.price 
            self.drunkenness += drink.alcohol_level
            if self.singing_ability > 0:
                self.singing_ability -= 1
            else:
                self.singing_ability = 0 
            if self.munchies_level < 15:
                self.munchies_level += 1
            else:
                self.munchies_level = 15
            if self.happy_mood <= (50 - (drink.alcohol_level)):
                self.happy_mood += (drink.alcohol_level)
            else:
                self.happy_mood -= (drink.alcohol_level / 2)

    def buy_snack(self, snack):
        self.wallet -= snack.price 
        if self.drunkenness < snack.sobering_effect:
            self.drunkenness = 0
        else:
            self.drunkenness -= snack.sobering_effect
        if self.munchies_level < snack.satiety_effect:
            self.munchies = 0 
        else: 
            self.munchies_level -= snack.satiety_effect 

    def check_into_room(self, room):
        self.wallet -= room.entry_fee 

    def sing_song(self, song):
        if self.favourite_song == song.name:
            if self.happy_mood <= 42:
                self.happy_mood += 8
            else:
                self.happy_mood = 50
        else:
            if self.happy_mood <= 46:
                self.happy_mood += 4
            else: self.happy_mood = 50
    
    def sees_favourite_song_in_playlist(self, room):
        for song in room.play_list:
            if song.name == self.favourite_song:
                self.happy_mood += 4
                return "Woohoo!"
        return "Darn. My favourite song's not here."
    
    def pay_room_tab(self, room):
        if self.wallet < room.room_tab:
            return "Sorry, you do not have sufficient funds."
        else:
            self.wallet -= room.room_tab 
        



    
        

    
    
        

    



        


