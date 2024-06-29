class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        original = list(nums)
        nums.sort()

        leftIndex = 0
        rightIndex = len(nums) - 1
        value = nums[leftIndex] + nums[rightIndex]

        while target != value:

            if target < value:
                rightIndex -= 1
            
            else:
                leftIndex += 1

            value = nums[leftIndex] + nums[rightIndex]

        leftFlag = 1
        rightFlag = 1

        for index, value in enumerate(original):
            if nums[leftIndex] == value and leftFlag == 1:
                leftIndex = index
                leftFlag = 0
            elif nums[rightIndex] == value and rightFlag == 1:
                rightIndex = index
                rightFlag = 0

            if rightFlag == 0 and leftFlag == 0:
                break

        return [min(leftIndex,rightIndex),max(leftIndex,rightIndex)]
