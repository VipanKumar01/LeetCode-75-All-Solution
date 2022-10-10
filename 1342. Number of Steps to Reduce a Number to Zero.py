# Name = Vipan Kumar
# GitHub user name = @VipanKumar01


class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        StepsCount = 0
        
        # Base Condition
        if num == 0:
            return 0
        
        # Main Code
        while(num>0):
            
            while num%2==0:
                num = num//2
                StepsCount += 1
                
            else:
                num -= 1
                StepsCount += 1
        
            if num==0:
                return StepsCount
            
            
# --HappyCode--
