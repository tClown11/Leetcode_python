class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        chars = dict()
        count = 0

        for i in range(len(s)):
            if s[i] in chars:
                left = max(left, chars[s[i]] + 1)
            chars[s[i]] = i
            count = max(count, i - left + 1)
        return count

if __name__ == "__main__":
    i = Solution()
    j = "pwwkew"
    i.lengthOfLongestSubstring(j)
