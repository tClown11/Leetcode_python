#344 Reverse String


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        beg = 0
        end = len(s) - 1
        while beg < end:
            s[beg], s[end] = s[end], s[beg]
            beg += 1
            end -= 1
        return s
