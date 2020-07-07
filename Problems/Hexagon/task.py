import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length


    # create get_area here
    def get_area(self):
        hexagon_according = (3 * math.sqrt(3) * pow(self.side_length, 2)) / 2
        return f'{hexagon_according:.3f}'
