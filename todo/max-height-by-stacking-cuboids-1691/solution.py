class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """

        cuboids = [sorted(box) for box in cuboids]
        cuboids.sort()

        gigacuboids = [[[h,w,l],[w,h,l],[l,w,h]] for l,w,h in cuboids]

        heights = [[box[0][2],box[1][2],box[2][2]] for box in gigacuboids]

        for i in range(len(cuboids)):
            maximum = [0,0,0]
            for j in range(i):
                for n in range(3):
                    for m in range(3):
                        if self.canBeStacked(gigacuboids[j][m], gigacuboids[i][n]):
                            if heights[j][m] > maximum[n]:
                                maximum[n] = heights[j][m]

            heights[i][0] += maximum[0]
            heights[i][1] += maximum[1]
            heights[i][2] += maximum[2]

        return max(max(h) for h in heights)

    def canBeStacked(self, b1, b2):
        return ((b1[0] <= b2[0] and b1[1] <= b2[1]) or (b1[0] <= b2[1] and b1[1] <= b2[0]))


sol = Solution()
cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
print(sol.maxHeight(cuboids))
