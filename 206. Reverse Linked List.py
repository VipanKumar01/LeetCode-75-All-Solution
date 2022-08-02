# Name = Vipan Kumar
# GitHub user name = @VipanKumar01


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = None
        current = head

        while current:
            next = current.next
            current.next = temp
            temp = current
            current = next

        return temp
      
# -- Happy Code --  
