from enum import Enum
class Ship:

    cardinal_dict = {0:"E",90:"N",180:"W",270:"S"}

    def __init__(self):

        self.X = 0 #posotive x values go east
        self.Y = 0 #posotive y values go north
        self.orientation = 0

        #then forward could just use the same input as our other method

    @staticmethod
    def normalize_degrees(degree):
        if degree >= 360:
            degree -= 360
        elif degree < 0:
            degree += 360

        return degree

    def alter_orientation(self,direction,degrees):

        if direction == "L":

            self.orientation += degrees
            self.orientation = Ship.normalize_degrees(self.orientation)

        elif direction == "R":

            self.orientation -= degrees
            self.orientation = Ship.normalize_degrees(self.orientation)

    def alter_global(self,direction,spaces):

        if direction == "E":
            self.X += spaces

        elif direction == "N":
            self.Y += spaces
        
        elif direction == "W":
            self.X -= spaces

        elif direction == "S":
            self.Y -= spaces

    def forward(self,spaces):

        direction = Ship.cardinal_dict[self.orientation]
        self.alter_global(direction,spaces)

    def display_loc(self):

        print(f"X: {self.X} Y: {self.Y}")

    def compute_man(self):

        return (abs(self.X) + abs(self.Y))
            