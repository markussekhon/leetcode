class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        middlepoint = lambda low, high : low + (high-low)//2

        while right-left != 1:
            middle = middlepoint(left, right)

            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle

        return min(nums[left],nums[right])

sol = Solution()
nums = [7,1,2,3,4,5,6]
print(sol.findMin(nums))
