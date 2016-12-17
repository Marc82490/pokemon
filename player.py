import random
from dice import *
from squares import *


class Player:
    """
    inputs: player name, a string
    
    Initializes a player.
    """
    def __init__(self, player_name):
        self.player_name = player_name
        self.miss_turn = False
        self.at_legendaries = False
        self.birds = 0
        self.elite = False
            
    def get_name(self):
        return self.player_name
    
    def set_missed_turn(self):
        self.miss_turn = True
    
    def get_missed_turn(self):
        return self.miss_turn
    
    def clear_missed_turn(self):
        self.miss_turn = False
    
    def set_at_legendaries(self):
        self.at_legendaries = True
        
    def get_at_legendaries(self):
        return self.at_legendaries
    
    def get_birds(self):
        return self.birds
        
    def add_bird(self):
        self.birds += 1
        
    def get_elite(self):
        return self.elite
    
    def set_elite(self):
        self.elite = True
