class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        end = len(intervals) - 1
        idx = 0
        intervals.sort()

        while idx < end:

            checkEnd = intervals[idx][1]
            checkStart = intervals[idx+1][0]

            if checkEnd >= checkStart:
                newStart = min(intervals[idx][0], intervals[idx+1][0])
                newEnd = max(intervals[idx][1], intervals[idx+1][1])

                intervals[idx] = [newStart, newEnd]
                intervals.pop(idx+1)

                end = len(intervals) - 1
            else:
                idx += 1

        return intervals

sol = Solution()
intervals = [[1,4],[0,0]]

print(sorted(intervals))
print(sol.merge(intervals))
