from climb_stairs import climbStairs


def test_cs():
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8


def test_1():
    assert climbStairs(1) == 1
    assert climbStairs(2) == 2
