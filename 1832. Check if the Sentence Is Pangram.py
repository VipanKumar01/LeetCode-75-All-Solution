# Name = Vipan Kumar
# user name = @VipanKumar01


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = "abcdefghijklmnopqrstuvwxyz"
        count = 0
        
        for letter in letters:
            if letter in sentence:
                count+=1
            else:
                count-=1
                
        if count == 26:
            return True
        else:
            return False
          
#   --HappyCode--
