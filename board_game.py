import random

def roll_dice():
    return random.randint(1,6)

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
        reg_squares = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18,
                        20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34,
                        35, 36, 37, 38, 39, 40, 41, 42, 44, 45, 46, 47, 48, 49,
                        50, 51, 53, 54, 55, 56, 57, 59, 60, 61, 62, 64, 65, 66,
                        67]
        gold_squares = [6, 13, 19, 32, 43, 52, 58, 63, 68, 69, 70, 71]
        for square in reg_squares:
            self.squares.append(BoardSquare(square))
        for square in gold_squares:
            self.squares.append(GoldSquare(square))
            
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
        if not self.gold_check(player) or self.get_square(player).check_visitor(player):
            for x in range(roll):
                self.players[player] += 1
                if self.gold_check(player):
                    if self.get_square(player).check_visitor(player):
                        continue                        
                    else:
                        self.check_special_action(player)
                        self.get_square(player).add_visitor(player)
                        break
    
    def check_special_action(self, player):
        if self.gold_check(player) and not self.get_square(player).check_visitor(player):
            self.get_square(player).special_actions(player)
            
    def next_turn(self):
        for player in self.roll_order:
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

class BoardSquare:
    """
    Announces any actions or drinks required for that square.
    Signals which player(s) is on its space.
    """
    def __init__(self, square_id):
        """
        square_id: an int, the squares spot on the board.
        """
        self.square_id = square_id
        self.gold = False
        
    def get_id(self):
        return self.square_id
    
    def check_visitor(self, player):
        """
        Regular board squares do not prevent players from moving forwards.
        """
        return True
        
    def special_actions(self, player):
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
        
    def add_visitor(self, player):
        """
        Records a player visiting this square.
        """
        self.visitors.append(player)
    
    def check_visitor(self, player):
        """
        Checks if a player has visited this square before.
        """
        return player in self.visitors
    
    def special_actions(self, player):
        if self.square_id == 6:                  # Pewter
            roll = roll_dice()
            print(roll)
        elif self.square_id == 13:               # Cerulean
            pass # no special actions
        elif self.square_id == 19:               # Vermilion
            roll = roll_dice()
            if roll % 2 == 0:
                player.set_missed_turn()
        elif self.square_id == 32:               # Celadon
            if roll_dice() <= 3:
                player.set_missed_turn()
        elif self.square_id == 43:               # Saffron
            prediction = int(input('Pick a number, 1-6: '))
            if roll_dice() == prediction:
                print(roll_dice())
        elif self.square_id == 52:               # Fuchsia
            pass # no special actions
        elif self.square_id == 58:               # Cinnabar
            while True:
                if roll_dice() % 2 == 0:
                    continue
                else:
                    break
        elif self.square_id == 63:               # Viridian
            pass # no special actions
        elif self.square_id == 68:               # Legendaries
            if player.get_legendaries() != 3:
                if roll_dice() >= 4:
                    player.add_legendary()
        elif self.square_id == 69:               # Elite Four
            while True:
                if roll_dice() != 4:
                    continue
                else:
                    break
        elif self.square_id == 70:               # Champion Gary
            pass # no special actions
        elif self.square_id == 71:               # Pokemon Master!
            pass # no special actions

class SilverSquare(BoardSquare):
    """
    Announces special rules for that zone when a player reaches it.
    """
    pass
    
class Player:
    """
    inputs: player name, a string
    
    Initializes a player.
    """
    def __init__(self, player_name):
        self.player_name = player_name
        self.miss_turn = False
        self.legendaries = 0
            
    def get_name(self):
        return self.player_name
    
    def set_missed_turn(self):
        self.miss_turn = True
    
    def get_missed_turn(self):
        return self.miss_turn
    
    def clear_missed_turn(self):
        self.miss_turn = False
    
    def get_legendaries(self):
        return self.legendaries
        
    def add_legendary(self):
        self.legendaries += 1
