class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    findTargetSumWays(nums, target) {

        function rec(i,currSum){
            if(i == nums.length)
                return currSum == target ? 1 : 0
            
            return (
                rec(i+1,currSum + nums[i]) + 
                rec(i+1,currSum - nums[i])
            )
        }

        return rec(0,0)
    }
}
