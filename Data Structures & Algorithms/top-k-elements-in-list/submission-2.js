class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, t) {
        const mp = new Map();
        const fr = new Map();
        for (const e of nums) {
            mp.set(e, (mp.get(e) || 0) + 1)
        }
        const res = new Array(1e4 + 1).fill(0)
        for (const [k, v] of mp.entries()) {
            res[v]++;
            if (fr.has(v)) {
                fr.set(v, [...fr.get(v), k])
            }else{
                fr.set(v,[k])
            }

        }
        const ans = []
        for (let j = 1e4; j >= 0; j--) {
            if (res[j] > 0)
                ans.push(...fr.get(j))
            if (ans.length === t)
                return ans
        }
    }
}
