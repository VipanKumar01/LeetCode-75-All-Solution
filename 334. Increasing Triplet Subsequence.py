# This Question is already posted In Java


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = math.inf
        second = math.inf

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:  # First < num <= second
                second = num
            else:
                return True  # First < second < num (third)

        return False
        
#   --HappyCode--
