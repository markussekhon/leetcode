class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        result = [[1]]

        for i in range(1,numRows):
            check = (0,i)
            row = [0] * (i+1)
            result.append(row)
            for j in range(i+1):
                if j in check:
                    result[i][j] = 1
                else:
                    result[i][j] += result[i-1][j-1] + result[i-1][j]
        return result


sol = Solution()
n = 1
m = 5
p = 50

print(sol.generate(n))
print(sol.generate(m))
print(sol.generate(p))
