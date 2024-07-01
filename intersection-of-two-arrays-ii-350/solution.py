class Solution():
    def intersection(self, nums1: list[int], nums2: list[int]):
        """
        :rtype: List[int]
        """

        map = dict()
        solve = []

        for value in nums1:
            if map.get(value):
                map[value] += 1
            else:
                map[value] = 1

        for value in nums2:
            if map.get(value) and map.get(value) > 0:
                map[value] -= 1
                solve.append(value)

        return solve

solution = Solution()
n1 = [1,2,2,1]
n2 = [2,2]
print(solution.intersection(n1,n2))
