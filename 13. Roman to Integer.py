# Name = Vipan Kumar
# user name = @VipanKumar01

romanDict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

class Solution:
    def romanToInt(self, S: str) -> int:
        result = 0
        
        for i in range(len(S)-1,-1,-1):
            num = romanDict[S[i]]
            if 4 * num < result: result -= num
            else: result += num
        return result

      
#   --HappyCode--
