class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()

        if s == "":
            return 0

        digits = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        result = 0
        neg = 1

        if s[0] == "-":
            neg = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        s = s + "%"

        for idx, ch in enumerate(s):
            if ch not in digits.keys():
                s = s[:idx]
                break

        for ch in s:
            idx -= 1
            result += pow(10, idx) * digits.get(ch,0)

        if result >= 2147483648:
            if neg == -1:
                result = 2147483648
            else:
                result = 2147483647

        return result * neg


sol = Solution()
s = " -1337"
print(sol.myAtoi(s))
