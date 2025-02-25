class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to convert a linked list to a list (for easy printing)
    def to_list(self):
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)  # Dummy node to start the result list
    current = dummy_head  # Pointer to construct the new list
    carry = 0  # Carry starts at 0

    # Loop until both lists are exhausted and no carry is left
    while l1 or l2 or carry:
        # Extract values or use 0 if the list is None
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Compute the sum and determine the carry
        total = val1 + val2 + carry
        carry = total // 10  # Carry for next step
        new_digit = total % 10  # Digit to store in the new node

        # Create a new node with new_digit and move the pointer
        current.next = ListNode(new_digit)
        current = current.next

        # Move l1 and l2 to the next nodes if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    # Return the next node of dummy_head (since dummy_head is just a placeholder)
    return dummy_head.next

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next  # Return the first real node

# Example 1: [2,4,3] + [5,6,4] = [7,0,8]
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])
result = addTwoNumbers(l1, l2)
print(result.to_list())  # Expected Output: [7, 0, 8]

# Example 2: [0] + [0] = [0]
l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = addTwoNumbers(l1, l2)
print(result.to_list())  # Expected Output: [0]

# Example 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
l1 = create_linked_list([9,9,9,9,9,9,9])
l2 = create_linked_list([9,9,9,9])
result = addTwoNumbers(l1, l2)
print(result.to_list())  # Expected Output: [8,9,9,9,0,0,0,1]
