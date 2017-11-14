# sample object oriented programming (OOP) - making UK coins (in pounds)

import random

class Pound:

    def __init__(self, rare=False): # constructor method - make the coins
        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.value = 1.00
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

    def __del__(self): # destructor method - spend the coins
        print("Coin spent!")

    def rust(self): # make your own method - the coin is rusty
        self.color = "greenish"

    def clean(self): # make your own method again - wipe the coin clean
        self.color = "gold"

    def flip(self): # flip the coin - heads or tails
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    
