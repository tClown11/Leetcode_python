import re

#Only the space character ' ' is considered as whitespace character.
#Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (231 − 1) or
# INT_MIN (−231) is returned.


class Solution:
    def myAtoi(self, str):
        str = str.strip()
        print(str)
        str = re.findall(r'(^[\+\-0]*\d+)\D*', str)
        print(str)

        try:
            result = int(''.join(str))
            print(result)
            MIN_INT = -2147483648
            MAX_INT = 2147483647

            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0



s = Solution()
y = "43"
print(s.myAtoi(y))