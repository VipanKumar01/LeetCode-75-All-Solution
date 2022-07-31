# Name = Vipan Kumar
# GitHub user name = @VipanKumar01


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
          
        temp = 0
        
        for char in t:
            if temp == len(s):
                return True
            
            elif char == s[temp]:
                temp += 1
                
        return temp == len(s)
      
# Name = Vipan Kumar
# GitHub user name = @VipanKumar01




# --HappyCode--
