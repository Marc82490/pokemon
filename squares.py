import random
from dice import *
from player import *


class BoardSquare:
    """
    Announces any actions or drinks required for that square.
    """
    def __init__(self, square_id):
        """
        square_id: an int, the squares spot on the board.
        """
        self.square_id = square_id
        self.gold = False
        self.silver = False
        
    def get_id(self):
        return self.square_id
    
    def check_visitor(self, player):
        """
        Regular board squares do not prevent players from moving forward.
        """
        return True
        
    def special_actions(self, player, roll):
        if self.get_id() == 1:                  # Rattata
            pass # no special actions
        elif self.get_id() == 2:                # Pidgey
            self.pidgey(player)
        elif self.get_id() == 3:                # Caterpie
            self.caterpie(player)
        elif self.get_id() == 4:                # Pikachu
            pass # no special actions
        elif self.get_id() == 5:                # Beedrill
            pass # no special actions
        elif self.get_id() == 7:                # Nidoran
            pass # no special actions
        elif self.get_id() == 8:                # Zubat
            self.zubat(player)
        elif self.get_id() == 9:                # Clefairy
            pass # no special actions
        elif self.get_id() == 10:               # Jigglypuff
            self.jigglypuff(player)
        elif self.get_id() == 11:               # Abra 1
            self.abra(player)
        elif self.get_id() == 12:               # Gary 1
            self.gary_one(player)
        elif self.get_id() == 14:               # Slowpoke
            pass # no special actions
        elif self.get_id() == 15:               # Bellsprout
            pass # no special actions
        elif self.get_id() == 16:               # Meowth
            pass # no special actions
        elif self.get_id() == 17:               # Diglett
            pass # no special actions
        elif self.get_id() == 18:               # S.S. Anne
            self.ss_anne(player)
        elif self.get_id() == 20:               # Bicycle
            self.bicycle(player)
        elif self.get_id() == 21:               # Magikarp
            self.magikarp(player)
        elif self.get_id() == 22:               # Sandshrew
            pass
        elif self.get_id() == 28:               # Abra 2
            self.abra(player)
        elif self.get_id() == 29:               # Snorlax
            pass # no special actions
        elif self.get_id() == 30:               # Gary 2
            self.gary_two(player)
        elif self.get_id() == 31:               # Eevee
            pass # no special actions
        elif self.get_id() == 33:               # Psyduck
            pass # no special actions
        elif self.get_id() == 34:               # Evolve
            self.evolve(player)
        elif self.get_id() == 35:               # Porygon
            pass # no special actions
        elif self.get_id() == 41:               # Rare Candy
            self.rare_candy(player)
        elif self.get_id() == 42:               # Gary 3
            self.gary_three(player)
        elif self.get_id() == 44:               # Hitmonchan
            self.hitmonchan(player)
        elif self.get_id() == 45:               # Krabby
            pass # no special actions
        elif self.get_id() == 46:               # Ditto
            pass # no special actions
        elif self.get_id() == 47:               # Doduo
            pass # no special actions
        elif self.get_id() == 53:               # Electrode
            pass # no special actions
        elif self.get_id() == 54:               # Electabuzz
            self.electabuzz(player)
        elif self.get_id() == 55:               # Poliwag
            pass # no special actions
        elif self.get_id() == 56:               # Seaking
            pass # no special actions
        elif self.get_id() == 57:               # Missingno
            self.missingno(player)
        elif self.get_id() == 59:               # Koffing
            pass # no special actions
        elif self.get_id() == 60:               # Fossil
            pass # no special actions
        elif self.get_id() == 61:               # Pokeball
            self.pokeball(player)
        elif self.get_id() == 62:               # Persian
            self.persian(player)
        elif self.get_id() == 64:               # Fearow
            pass # no special actions
        elif self.get_id() == 65:               # Graveler
            self.graveler(player)
        elif self.get_id() == 66:               # Gyrados
            self.gyrados(player)
        elif self.get_id() == 67:               # Dragonite
            self.dragonite(player)
        
    def pidgey(self, player):
        pass
    
    def caterpie(self, player):
        pass

    def zubat(self, player):
        pass
        
    def jigglypuff(self, player):
        pass
    
    def abra(self, player):
        pass
        
    def gary_one(self, player):
        pass
        
    def ss_anne(self, player):
        pass
    
    def bicycle(self, player):
        pass
    
    def magikarp(self, player):
        pass
    
    def gary_two(self, player):
        pass
        
    def evolve(self, player):
        pass
        
    def rare_candy(self, player):
        pass
        
    def gary_three(self, player):
        pass
    
    def hitmonchan(self, player):
        pass
        
    def electabuzz(self, player):
        pass
        
    def missingno(self, player):
        pass
        
    def pokeball(self, player):
        pass
        
    def persian(self, player):
        pass
        
    def graveler(self, player):
        pass
        
    def gyrados(self, player):
        pass
        
    def dragonite(self, player):
        pass
        
class GoldSquare(BoardSquare):
    """
    Prevents a player from moving forward until a certain action is accomplished.
    Keeps track of which players have visited this space.
    """
    def __init__(self, square_id):
        """
        square_id: an int, the squares spot on the board.
        """
        self.square_id = square_id
        self.visitors = []
        self.gold = True
        self.silver = False
        
    def add_visitor(self, player):
        """
        Records a player visiting this square.
        """
        if self.square_id == 68:
            if player.get_birds() == 3:
                self.visitors.append(player)
        elif self.square_id == 69:
            if player.get_elite():
                self.visitors.append(player)
        else:
            self.visitors.append(player)
    
    def check_visitor(self, player):
        """
        Checks if a player has visited this square before.
        """
        return player in self.visitors
    
    def special_actions(self, player, roll):
        if self.square_id == 6:                  # Pewter
            self.pewter(player)
        elif self.get_id() == 13:               # Cerulean
            pass # no special actions
        elif self.get_id() == 19:               # Vermilion
            self.vermilion(player)
        elif self.get_id() == 32:               # Celadon
            self.celadon(player)
        elif self.get_id() == 43:               # Saffron
            self.saffron(player)
        elif self.get_id() == 52:               # Fuchsia
            pass # no special actions
        elif self.get_id() == 58:               # Cinnabar
            self.cinnabar(player)
        elif self.get_id() == 63:               # Viridian
            pass # no special actions
        elif self.get_id() == 68:               # Legendaries
            self.legendaries(player, roll)
        elif self.get_id() == 69:               # Elite Four
            self.elite_four(player, roll)
        elif self.get_id() == 70:               # Champion Gary
            pass # no special actions
        elif self.get_id() == 71:               # Pokemon Master!
            pass # no special actions

    def pewter(self, player):
        loc_roll = roll_dice()
        print(loc_roll, 'Pewter')
    
    def vermilion(self, player):
        loc_roll = roll_dice()
        print(loc_roll, 'Vermilion')
        if loc_roll % 2 == 0:
            player.set_missed_turn()
            
    def celadon(self, player):
        loc_roll = roll_dice()
        print(loc_roll, 'Celadon')
        if loc_roll <= 3:
            player.set_missed_turn()
            
    def saffron(self, player):
        while True:
            try:
                prediction = int(input("Pick a number between 1 and 6: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if prediction not in range(1, 7):
                print("Please enter a valid number.")
                continue
            else:
                break
        loc_roll = roll_dice()
        if loc_roll == prediction:
            print(loc_roll, 'Saffron')
            
    def cinnabar(self, player):
        while True:
            loc_roll = roll_dice()
            print(loc_roll, 'Cinnabar')
            if loc_roll % 2 == 0:
                continue
            else:
                break
                
    def legendaries(self, player, roll):
        if not player.get_at_legendaries():
            print('Got to Legendaries')
            loc_roll = roll_dice()
            print(roll, 'First roll at Legendaries')
            if roll >= 4:
                player.add_bird()
                print('Added bird')
            player.set_at_legendaries()
        elif player.get_at_legendaries() and player.get_birds() != 3:
            print('Already at Legendaries')
            if roll >= 4:
                player.add_bird()
                print('Added bird')
        else:
            pass
            
    def elite_four(self, player, roll):
        if roll != 4:
            print('Not Elite!')
        else:
            player.set_elite()
            print('Elite!')
            
class SilverSquare(BoardSquare):
    """
    Announces special rules for that zone when a player reaches it.
    """
    def __init__(self, square_id):
        """
        square_id: an int, the squares spot on the board.
        """
        self.square_id = square_id
        self.gold = False
        self.silver = True
    
    def special_actions(self, player, roll):
        if self.get_id() == 23:                 # Pokemon Tower
            pass # no special actions
        elif self.get_id() == 24:               # Channeler
            pass # no special actions
        elif self.get_id() == 25:               # Haunter
            self.haunter(player)
        elif self.get_id() == 26:               # Cubone
            pass # no special actions
        elif self.get_id() == 27:               # Silph Scope
            pass # no special actions
        elif self.get_id() == 36:               # Silph Co.
            pass # no special actions
        elif self.get_id() == 37:               # Scientist
            pass # no special actions
        elif self.get_id() == 38:               # Lapras
            self.lapras(player)
        elif self.get_id() == 39:               # Team Rocket
            pass # no special actions
        elif self.get_id() == 40:               # Giovanni
            self.giovanni(player)
        elif self.get_id() == 48:               # Safari Zone
            pass # no special actions
        elif self.get_id() == 49:               # Dratini
            self.dratini(player)
        elif self.get_id() == 50:               # Taurus
            pass # no special actions
        elif self.get_id() == 51:               # Chansey
            self.chansey(player)
            
    def haunter(self, player):
        pass
    
    def lapras(self, player):
        pass
    
    def giovanni(self, player):
        pass
        
    def dratini(self, player):
        pass
    
    def chansey(self, player):
        pass
