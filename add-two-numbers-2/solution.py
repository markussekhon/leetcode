# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        returnNode = ListNode()
        carryValue = 0
        currentNode = returnNode


        while l1 is not None or l2 is not None:

            currentNode.next = ListNode(0)
            currentNode = currentNode.next

            currentNode.val += carryValue
            carryValue = 0

            if l1 is not None:
                currentNode.val += l1.val
                l1 = l1.next

            if l2 is not None:
                currentNode.val += l2.val
                l2 = l2.next

            if currentNode.val >= 10:
                carryValue = 1
                currentNode.val -= 10

        if carryValue == 1:
            currentNode.next = ListNode(1)

        return returnNode.next
