class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {number}
     */
    minDistance(word1, word2) {

        const dp = new Map()

        function dis(i=0,j=0){
            const k = [i,j].toString()

            if(dp.has(k))
                return dp.get(k)

            if(word2.length == j || word1.length == i)
                return word1.length - i + word2.length - j

          

            if(word1[i] == word2[j]){
                dp.set(k,dis(i+1,j+1))
                return dp.get(k)
            }

            const res = [
                1 + dis(i,j+1), 
                1+ dis(i+1,j+1),
                1 + dis(i+1,j)
            ]

            dp.set(k,Math.min(...res))
            return dp.get(k)
        }

        return dis()
    }
}
