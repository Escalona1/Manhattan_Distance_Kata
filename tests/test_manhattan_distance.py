from source.manhattan_distance import Point, manhattanDistance


def test_aligned_points():
    p1 = Point(1,1)
    p2 = Point(1,3)
    p3 = Point(1,5)

    assert manhattanDistance(p1, p2) == 2
    assert manhattanDistance(p1, p3) == 4