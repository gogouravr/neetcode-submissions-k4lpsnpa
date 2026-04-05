class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    findTargetSumWays(nums, target) {

        const dp = new Map();

        function rec(i,currSum){
            const memoKey = [i,currSum].toString()

            if(dp.has(memoKey))
                return dp.get(memoKey)

            if(i == nums.length)
                return currSum == target ? 1 : 0

            dp[memoKey] =  (
                rec(i+1,currSum + nums[i]) + 
                rec(i+1,currSum - nums[i])
            )

            return dp[memoKey]
        }

        return rec(0,0)
    }
}
