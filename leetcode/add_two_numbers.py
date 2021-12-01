from dataclasses import dataclass
from typing import Optional


MaybeNode = Optional["ListNode"]


@dataclass
class ListNode:
    val: int = 0
    # https://stackoverflow.com/a/36193829
    next: MaybeNode = None


def add_two_numbers(l1: MaybeNode, l2: MaybeNode) -> MaybeNode:
    """
    You are given two non-empty linked lists representing two non-negative
    integers. The digits are stored in reverse order, and each of their nodes
    contains a single digit. Add the two numbers and return the sum as a linked
    list.

    You may assume the two numbers do not contain any leading zero, except the
    number 0 itself.

    Constraints:
    - The number of nodes in each linked list is in the range [1, 100].
    - 0 <= Node.val <= 9
    - It is guaranteed that the list represents a number that does not have
      leading zeros.

    Source: https://leetcode.com/problems/add-two-numbers/
    """
    if not (l1 or l2):
        return None

    rv = ListNode()
    current = rv
    carry = 0

    while l1 or l2:
        val = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)

        carry = val // 10
        val %= 10

        current.val = val
        current.next = ListNode()
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return rv
