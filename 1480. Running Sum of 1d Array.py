# Name = Vipan Kumar
# GitHub user name = @VipanKumar01



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        runningSum = [0]*len(nums)
        Sum1 = 0
        
        for i in range(len(nums)):
            Sum1 = Sum1 + nums[i]
            runningSum[i] = Sum1
        return runningSum
        
        
        
    # -- Happy Code --
