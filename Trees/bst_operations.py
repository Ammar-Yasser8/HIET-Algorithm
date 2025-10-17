"""
Binary Search Tree Operations
Basic operations on a binary search tree.
Time Complexity: O(h) where h is height
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_bst(root, val):
    """Insert a value into BST."""
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    
    return root


def search_bst(root, val):
    """Search for a value in BST."""
    if not root or root.val == val:
        return root
    
    if val < root.val:
        return search_bst(root.left, val)
    return search_bst(root.right, val)


def inorder(root):
    """Helper function for inorder traversal."""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


if __name__ == "__main__":
    # Example usage
    root = None
    values = [5, 3, 7, 1, 4, 6, 9]
    
    for val in values:
        root = insert_bst(root, val)
    
    print(f"BST inorder traversal: {inorder(root)}")  # [1, 3, 4, 5, 6, 7, 9]
    
    search_val = 4
    result = search_bst(root, search_val)
    print(f"Search for {search_val}: {'Found' if result else 'Not found'}")
