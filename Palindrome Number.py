#9  Palindrome Number


class Solution:
    def isPalindrome(self, x):
        s = str(x)
        beg, end = 0, len(s)-1

        while beg < end:
            if s[beg] == s[end]:
                beg += 1
                end -= 1
            else:
                return False
        return True
