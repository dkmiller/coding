from pytest import mark
from two_sum import two_sum


@mark.parametrize("nums,target,expected", [([2, 7, 11, 15], 9, [0, 1])])
def test_two_sum(nums, target, expected):
    actual = two_sum(nums, target)

    # https://stackoverflow.com/a/9623147
    assert set(expected) == set(actual)
