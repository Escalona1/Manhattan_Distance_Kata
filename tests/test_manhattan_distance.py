from source.manhattan_distance import Point

def test_1():
    p1 = Point(1,1)
    p2 = Point(2,2)

    assert p1.manhattanDistance(p2) == 1