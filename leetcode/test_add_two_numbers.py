from add_two_numbers import MaybeNode, add_two_numbers, ListNode
from pytest import mark


def to_list_node(num: int) -> ListNode:
    rv = ListNode()

    while num:
        rv.val = num % 10
        rv.next = ListNode()
        rv = rv.next
        num //= 10

    return rv


def from_list_node(node: MaybeNode) -> int:
    rv = 0
    base = 0

    while node:
        rv += node.val * base
        base *= 10

    return rv


@mark.parametrize(
    "l1,l2,expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    l1 = to_list_node(l1)
    l2 = to_list_node(l2)
    rv = add_two_numbers(l1, l2)
    rv = from_list_node(rv)
    assert expected == rv
