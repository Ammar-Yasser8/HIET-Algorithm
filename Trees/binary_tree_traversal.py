"""
Binary Tree Traversal Algorithms
Different ways to traverse a binary tree.
Time Complexity: O(n) for all traversals
Space Complexity: O(h) where h is height
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """Left -> Root -> Right"""
    result = []
    if root:
        result.extend(inorder_traversal(root.left))
        result.append(root.val)
        result.extend(inorder_traversal(root.right))
    return result


def preorder_traversal(root):
    """Root -> Left -> Right"""
    result = []
    if root:
        result.append(root.val)
        result.extend(preorder_traversal(root.left))
        result.extend(preorder_traversal(root.right))
    return result


def postorder_traversal(root):
    """Left -> Right -> Root"""
    result = []
    if root:
        result.extend(postorder_traversal(root.left))
        result.extend(postorder_traversal(root.right))
        result.append(root.val)
    return result


if __name__ == "__main__":
    # Example usage: Create a simple binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print(f"Inorder: {inorder_traversal(root)}")    # [4, 2, 5, 1, 3]
    print(f"Preorder: {preorder_traversal(root)}")  # [1, 2, 4, 5, 3]
    print(f"Postorder: {postorder_traversal(root)}")  # [4, 5, 2, 3, 1]
