class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next
        while (slow and fast and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False