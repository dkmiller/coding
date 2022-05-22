# https://stackoverflow.com/a/69802572
from __future__ import annotations

from dataclasses import dataclass
from math import inf
from queue import Queue
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


# Runtime: 170 ms, memory Usage: 16.7 MB.
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """
    Given the root of a binary tree, determine if it is a valid binary search
    tree (BST).

    A valid BST is defined as follows:

    - The left subtree of a node contains only nodes with keys less than the
      node's key.
    - The right subtree of a node contains only nodes with keys greater than the
      node's key.
    - Both the left and right subtrees must also be binary search trees.

    Taken from:
    https://leetcode.com/problems/validate-binary-search-tree/
    """
    queue = Queue()
    if root:
        queue.put([root, -inf, inf])

    while not queue.empty():
        (node, lower, upper) = queue.get()
        if node:
            if not lower < node.val < upper:
                return False
            queue.put([node.left, lower, node.val])
            queue.put([node.right, node.val, upper])

    return True
