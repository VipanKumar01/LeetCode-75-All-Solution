//  Name = Vipan Kumar
//  GitHub user name = @VipanKumar01



class Solution {
    public int pivotIndex(int[] nums) {
        // int total = 0;
        
        final int total = Arrays.stream(nums).sum();
        
        // You can also use this -->>
        // for(int i=0;i<nums.length;i++){
        //     total += nums[i];
        // }

      
//  Name = Vipan Kumar
//  GitHub user name = @VipanKumar01
      
        int leftIdxs = 0;
        int rightIdxs = total;
        
        for(int i=0;i<nums.length;i++){
            if (rightIdxs - leftIdxs - nums[i] == leftIdxs)
                return i;
                leftIdxs  += nums[i];
        }
        return -1;

    }
}


//  -- Happy Code --
