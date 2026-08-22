# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        if not head:
            return False

        seen[head] = 1
        
        while head and head.next:
            if head.next in seen:
                return True
            else:
                seen[head.next] = head.next
                head = head.next
        
        return False