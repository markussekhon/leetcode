class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """

        map = set()
        index = 0

        while index < len(nums):

            start = nums[index][0]
            end = nums[index][1] + 1

            for value in range(start, end):
                map.add(value)

            index += 1
        return len(map)

sol = Solution()
nums = [[3,6],[1,5],[4,7]]
print(sol.numberOfPoints(nums))
