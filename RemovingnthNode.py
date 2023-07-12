class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Calculate the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Find the position of the node to remove
        position = length - n

        # Traverse to the node before the one to be removed
        prev = dummy
        for _ in range(position):
            prev = prev.next

        # Remove the nth node
        prev.next = prev.next.next

        # Return the head of the modified linked list
        return dummy.next
