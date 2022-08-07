# Name = Vipan Kumar
# GitHub user name = @VipanKumar01


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tort = head
        hare = head
        
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            
            if tort == hare:
                tort = head
                
                while tort != hare:
                    tort = tort.next
                    hare = hare.next
                    
                if tort == hare:
                    return tort
                
        return None
      
      
# -- Happy Code --
