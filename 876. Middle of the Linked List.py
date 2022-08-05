# Name = Vipan Kumar
# GitHub user name = @VipanKumar01



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tort = hare = head
        
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            
        return tort
      
# -- Happy Code --
