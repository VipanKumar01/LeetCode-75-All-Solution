// In this Question I am taking Two Integers that contains already Maximum Integer Value 
// After that I am Compare the values with Max and List Indexes 


class Solution {
    public boolean increasingTriplet(int[] nums) {
        int Max1 = Integer.MAX_VALUE; // It Contains Max Values
        int Max2 = Integer.MAX_VALUE; // It Contains Max Values
        
        // ForEach Loop Traverse All the elements of array/list
        for(int n : nums)
        {
            if(n<=Max1)
                Max1 = n;
            else if(n<=Max2)
                Max2 = n;
            else 
                return true;    
        }
        return false;
    }
}


//   --HappyCode--
