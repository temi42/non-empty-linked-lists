class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head = None
        current = None

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            totalvalues = value1 + value2 + carry 

            #if carry >= 10:
            carry = totalvalues // 10
            newnum = totalvalues % 10

            new_node = ListNode(newnum)


            if head is None:
                head  = new_node
                current = new_node
            else:
                current.next = new_node
                current = new_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head 

