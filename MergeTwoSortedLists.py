# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        head = ListNode()
        looper = head
        tail = None

        while(list1 and list2):
            if(list1.val <= list2.val):
                looper.next = list1
                looper = looper.next
                list1 = list1.next
                tail = list2
            else:
                looper.next = list2
                looper = looper.next
                list2 = list2.next
                tail = list1
            

        looper.next = tail
        return head.next


        
~
~
~
~
~
~
