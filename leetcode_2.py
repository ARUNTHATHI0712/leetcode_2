class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to help simplify edge cases
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists
        while l1 is not None or l2 is not None or carry:
            # Get the current values from each list (0 if the list is exhausted)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the current digits and carry
            total = val1 + val2 + carry
            
            # Update carry for the next iteration
            carry = total // 10
            
            # Create a new node with the sum's last digit
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes in each list
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next node of dummy_head (which is the actual head of the result list)
        return dummy_head.next
# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])

# Create an instance of Solution and call addTwoNumbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Convert the result to a list and print it
print(linkedlist_to_list(result))  # Output: [7, 0, 8]
