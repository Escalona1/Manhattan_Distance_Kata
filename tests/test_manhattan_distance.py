from source.manhattan_distance import Point, manhattanDistance


def test_1():
    p1 = Point(1,1)
    p2 = Point(2,2)

    assert  manhattanDistance(p1, p2) == 1