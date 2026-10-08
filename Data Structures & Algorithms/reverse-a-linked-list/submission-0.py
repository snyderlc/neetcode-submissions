# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        if current is None:
            return 

        while current:
            stack.append(current)
            current = current.next
        
        for i in range(1, len(stack)):
            stack[i].next = stack[i - 1]

        stack[0].next = None

        return stack[-1]
        
        
        