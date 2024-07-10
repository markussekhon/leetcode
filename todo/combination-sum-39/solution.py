class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if target == 0:
            return []

        if target < 0:
            return None

        for value in candidates:
            if value <= target:
                subtarget = target - value
                result = self.combinationSum(candidates, subtarget)

                if result is not None:
                    return [value, *result]


sol = Solution()
can = [2,3,6,7]
target = 7
print(sol.combinationSum(can,target))
