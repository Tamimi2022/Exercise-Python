# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
# Part 1  Player.__init__
class Player:
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if 0 < speed < 1:
            self.speed = speed
        if 0 < endurance < 1:
            self.endurance = endurance
        if 0 < accuracy < 1:
            self.accuracy = accuracy
        else:
            raise ValueError("If not between [0, 1]")
        
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        
#  Player.introduce
    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

# Player.strength
    def strength(self):
        if self.speed >= self.endurance and self.speed >= self.accuracy:
            return ('speed', self.speed)
        elif self.endurance > self.speed and self.endurance >= self.accuracy:
            return ('endurance', self.endurance)
        else:
            return ('accuracy', self.accuracy)
        
        #speed > endurance > accuracy

# Part 2 Commentator
class Commentator:
    def __init__(self, name):
        self.name = name
#ray = Commentator('Ray Hudson')
#print(ray.name)

#  sum_player
    def sum_player(self, y):
        return sum(
            [getattr(y, 'speed'), getattr(y, 'endurance'), getattr(y, 'accuracy')]
        )
        
#  Compare Players
    def compare_players(self, player1, player2, attr):
        player1_attr = getattr(player1, attr)
        player2_attr = getattr(player1, attr)

        # First comparison
        if player1_attr > player2_attr:
            return player1.name
        elif player2_attr > player1_attr:
            return player2.name

        # Second case
        player1_strength = player1.strength()[1]
        player2_strength = player2.strength()[1]
        if player1_strength > player2_strength:
            return player1.name
        elif player2_strength > player1_strength:
            return player2.name

        # Third case
        if self.sum_player(player1) > self.sum_player(player2):
            return player1.name
        elif self.sum_player(player2) > self.sum_player(player1):
            return player2.name
        
        # If these are also equal, return the string:
        return 'These two players might as well be twins!'
        
        
if __name__ == '__main__':
    pass