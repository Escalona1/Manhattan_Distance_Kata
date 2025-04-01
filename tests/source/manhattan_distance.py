class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattanDistance(self, other):
        return other.y - self.y


def manhattanDistance(Point1, Point2):
    return Point1.manhattanDistance(Point2)

        
