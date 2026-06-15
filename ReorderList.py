# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        temp_head = head
        num_nodes = 0
        while(temp_head is not None):
            num_nodes += 1
            temp_head = temp_head.next

        if(num_nodes == 1):
            return head

        temp_head = head
        mid_node = None
        for i in range(num_nodes/2):
            mid_node = temp_head
            temp_head = temp_head.next

        second_half = mid_node.next
        mid_node.next = None

        #reverse the tide!
        curr = second_half
        prev = None
        # print("traversing second half")
        while curr is not None:
            # print(curr.val)
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node


        head1 = head
        head2 = prev
        print("Combining")
        final_node = None
        while head2 is not None and head1 is not None:
            # print(head1.val, head2.val)
            next_h1 = head1.next
            head1.next = head2
            next_h2 = head2.next
            head2.next = next_h1
            final_node = head1
            head1 = next_h1
            head2 = next_h2
        
        if(head2):
            final_node = final_node.next
            final_node.next = head2


        return head
            
        
