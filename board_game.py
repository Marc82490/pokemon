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
        # If the current square is gold and they have not visited before,
        else:
            # check the square's action. Once this turn is complete, 
            self.check_special_action(player, roll)
            # mark them as having visited (if applicable).
            self.get_square(player).add_visitor(player)
    
    def check_special_action(self, player, roll):
        if self.gold_check(player) and not self.get_square(player).check_visitor(player):
            self.get_square(player).special_actions(player, roll)
            
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
        self.silver = False
        
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
            loc_roll = roll_dice()
            print(loc_roll, 'Pewter')
        elif self.square_id == 13:               # Cerulean
            pass # no special actions
        elif self.square_id == 19:               # Vermilion
            loc_roll = roll_dice()
            print(loc_roll, 'Vermilion')
            if loc_roll % 2 == 0:
                player.set_missed_turn()
        elif self.square_id == 32:               # Celadon
            loc_roll = roll_dice()
            print(loc_roll, 'Celadon')
            if loc_roll <= 3:
                player.set_missed_turn()
        elif self.square_id == 43:               # Saffron
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
        elif self.square_id == 52:               # Fuchsia
            pass # no special actions
        elif self.square_id == 58:               # Cinnabar
            while True:
                loc_roll = roll_dice()
                print(loc_roll, 'Cinnabar')
                if loc_roll % 2 == 0:
                    continue
                else:
                    break
        elif self.square_id == 63:               # Viridian
            pass # no special actions
        elif self.square_id == 68:               # Legendaries
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
        elif self.square_id == 69:               # Elite Four
            if roll != 4:
                print('Not Elite!')
            else:
                player.set_elite()
                print('Elite!')
        elif self.square_id == 70:               # Champion Gary
            pass # no special actions
        elif self.square_id == 71:               # Pokemon Master!
            pass # no special actions

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
    
    def special_actions(self, player):
        pass
    
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

