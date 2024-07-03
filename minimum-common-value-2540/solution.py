class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        nums1.sort()
        nums2.sort()

        rolodex = set()

        for val in nums1:
            rolodex.add(val)
        
        for val in nums2:
            if val in rolodex:
                return val
        
        return -1
