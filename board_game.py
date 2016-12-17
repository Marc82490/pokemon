import random
from dice import *
from squares import *
from player import *


class Board:
    """
    Adds players to the board.
    Randomizes the roll order.
    Moves player according to their roll(s) and any square specific rules.
    Keeps track of player positions on the board.
    Ends the game once 1 player reaches the end.
    """
    def __init__(self):
        """
        Initialize the game board.
        """
        self.squares = []
        self.roll_order = []
        self.players = {}
        self.game_end = False
    
    def add_squares(self):
        """
        Adds the squares to the board.
        """           
        gold_squares = [6, 13, 19, 32, 43, 52, 58, 63, 68, 69, 70, 71]
        silver_squares = [23, 24, 25, 26, 27, 36, 37, 38, 39, 40, 48, 49, 50, 51]
        
        for square in range(72):
            if square in gold_squares:
                self.squares.append(GoldSquare(square))
            elif square in silver_squares:
                self.squares.append(SilverSquare(square))
            else:
                self.squares.append(BoardSquare(square))
            
    def get_square(self, player):
        """
        Returns the square that the player is on.
        """
        for square in self.squares:
            if self.players[player] == square.get_id():
                return square

    def add_players(self, players):
        """        
        Adds the players to the game and starts them at the first square.
        
        players: a list of instances of class Player
        """
        for player in players:
            self.players[Player(player)] = 0

    def randomize_order(self):
        """
        Randomly chooses the roll order.
        """
        temp_list = []
        for player in self.players.keys():
            temp_list.append(player)
        for elem in range(len(temp_list)):
            player = random.choice(temp_list)
            self.roll_order.append(player)
            temp_list.remove(player)

    def gold_check(self, player):
        """
        Checks if a given player is on a gold square.
        
        player: an instance of Player class.
        
        Returns: True if the player is on a gold square.
        """
        for square in self.squares:
            if square.get_id() == self.players[player]:
                return square.gold
        
    def move_player(self, player, roll):
        """
        Moves a player forward, unless they encounter a gold square they have
        not visited before.
        
        player: an instance of Player class.
        roll: the results of a call to roll die.
        """
        # Checks that the current square is not gold or that they've visited before.
        if not self.gold_check(player) or self.get_square(player).check_visitor(player):
            # Move the player forward 1 square at a time.
            for x in range(roll):
                self.players[player] += 1
                # If they encounter a gold square, 
                if self.gold_check(player):
                    # check if they've visited before.
                    if self.get_square(player).check_visitor(player):
                        # If they have, keep moving.
                        continue                        
                    else:
                        # If they have not, check the square's action.
                        self.check_special_action(player, roll)
                        # After this turn's action is complete, mark them as
                        #  having visited (if applicable).
                        self.get_square(player).add_visitor(player)
                        break
            # If they do not encounter a gold square, check the special action
            #  of the final square they land on.
            self.check_special_action(player, roll)
        # If the current square is gold and they have not visited before,
        else:
            # check the square's action. Once this turn is complete, 
            self.check_special_action(player, roll)
            # mark them as having visited (if applicable).
            self.get_square(player).add_visitor(player)
    
    def check_special_action(self, player, roll):
        if self.gold_check(player):
            if not self.get_square(player).check_visitor(player):
                self.get_square(player).special_actions(player, roll)
        else:
            self.get_square(player).special_actions(player, roll)
            
    def next_turn(self):
        for player in self.roll_order:
            self.check_game_end()
            if self.get_game_end():
                print('STOP')
                break
            if not player.get_missed_turn():
                roll = roll_dice()
                print(roll)
                self.move_player(player, roll)
            else:
                print("Missed turn!")
                player.clear_missed_turn()
            
    
    def check_game_end(self):
        """
        Checks if a player has reached the last square.
        """
        for player in self.players:
            if self.players[player] == 71:
                self.game_end = True
                
    def get_game_end(self):
        """
        Returns True if the game is over.
        """
        return self.game_end
