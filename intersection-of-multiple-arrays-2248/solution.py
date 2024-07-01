class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        numOfArrays = len(nums)
        index = 1

        mySet = set()

        for value in nums[0]:
            mySet.add(value)

        while index < numOfArrays:
            curSet = set()
            for value in nums[index]:
                if value in mySet:
                    curSet.add(value)
            mySet = curSet
            index += 1

        return sorted(list(mySet))

sol = Solution()
nums = [[0,1,0],[1,0],[1,2,3]]
print(sol.intersection(nums))
