from pytest import mark
from validate_binary_search_tree import is_valid_bst, TreeNode


@mark.parametrize(
    "root,expected",
    [
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    ],
)
def test_is_valid_bst(root, expected):
    rv = is_valid_bst(root)
    assert expected == rv
