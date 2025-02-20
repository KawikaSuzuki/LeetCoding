# Define the ListNode class for the linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the solution class with the middleNode method.
class Solution:
    def middleNode(self, head):
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

# Helper function to create a linked list from a list.
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list.
def print_linked_list(head):
    current = head
    output = []
    while current:
        output.append(str(current.val))
        current = current.next
    print(" -> ".join(output))

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    
    # Initialize the solution and get the middle node.
    solution = Solution()
    middle = solution.middleNode(head)
    
    # Print the linked list starting from the middle node.
    print_linked_list(middle)
