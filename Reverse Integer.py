class Solution:
    def reverse(self, x):
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r*(r < 2**31)


i = Solution()
s = 123
y = -123
print(i.reverse(s))
print(i.reverse(y))
