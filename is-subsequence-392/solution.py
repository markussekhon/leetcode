class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0:
            return True
        elif len(t) == 0 or len(s) > len(t):
            return False

        si = 0
        ti = 0

        while True:

            if ti >= len(t):
                return False
            elif s[si] == t[ti]:
                si += 1
            
            ti += 1
            
            if si >= len(s):
                return True
            elif ti >= len(t):
                return False
