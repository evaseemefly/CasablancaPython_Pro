import random
import Player
class Computer(Player.PlayerClass):
    def __repr__(self):
        return 'Computer(%s)'%str(self)
    def get_move(self):
        return random.randint(1,10)