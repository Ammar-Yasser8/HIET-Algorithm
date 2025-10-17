"""
Detect Cycle in Linked List
Detect if a linked list has a cycle using Floyd's cycle detection.
Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """
    Detect if linked list has a cycle using two pointers.
    
    Args:
        head: Head of linked list
    
    Returns:
        True if cycle exists, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True


if __name__ == "__main__":
    # Example usage: Create list with cycle
    # 1 -> 2 -> 3 -> 4
    #      ^         |
    #      |_________|
    
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next  # Create cycle
    
    print(f"Has cycle: {has_cycle(head)}")  # True
    
    # Example without cycle
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    
    print(f"Has cycle: {has_cycle(head2)}")  # False
