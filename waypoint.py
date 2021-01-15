import math

class Waypoint:

    def __init__(self):

        self.X = 10
        self.Y = 1

    def rotate(self,direction,degrees):

        #left is clockwise, right is counterclockwise

        if direction == "R":

            degrees = 360 - degrees

        print(degrees)
        radians = math.radians(degrees)
        print(radians)

        old_X = self.X
        old_Y = self.Y

        self.X = (old_X * math.cos(radians)) - (old_Y * math.sin(radians))
        self.Y = (old_X * math.sin(radians)) + (old_Y * math.cos(radians))

    def shift(self,direction,spaces):

        if direction == "E":
            self.X += spaces

        elif direction == "N":
            self.Y += spaces

        elif direction == "W":
            self.X -= spaces

        elif direction == "S":
            self.Y -= spaces

    def get_x(self):

        return self.X

    def get_y(self):

        return self.Y

        
