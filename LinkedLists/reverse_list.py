"""
Reverse Linked List
Reverse a singly linked list.
Time Complexity: O(n)
Space Complexity: O(1) for iterative, O(n) for recursive
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_iterative(head):
    """
    Reverse linked list iteratively.
    
    Args:
        head: Head of linked list
    
    Returns:
        New head of reversed list
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev


def reverse_list_recursive(head):
    """
    Reverse linked list recursively.
    
    Args:
        head: Head of linked list
    
    Returns:
        New head of reversed list
    """
    if not head or not head.next:
        return head
    
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    
    return new_head


def print_list(head):
    """Helper function to print list."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


if __name__ == "__main__":
    # Example usage: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    
    print(f"Original list: {print_list(head)}")
    
    reversed_head = reverse_list_iterative(head)
    print(f"Reversed list: {print_list(reversed_head)}")
