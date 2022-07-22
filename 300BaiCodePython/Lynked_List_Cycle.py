class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
		
        s = head
        f = head

        while True:

            if f.next is None or f.next.next is None:
                return False

            s = s.next
            f = f.next.next

            if s == f:
                return True