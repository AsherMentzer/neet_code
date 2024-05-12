from min_cost import minCostClimbingStairs


def test_min():
    assert minCostClimbingStairs([10, 15, 20]) == 15
    assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
