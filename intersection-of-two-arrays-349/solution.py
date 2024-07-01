class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        map = dict()
        solve = []

        for value in nums1:
            map[value] = 1

        for value in nums2:
            if map.get(value,0) > 0:
                map[value] = 0
                solve.append(value)

        return solve


solution = Solution()
n1 = [2,2]
n2 = [1,2,2,1]
print(solution.intersection(n1,n2))
