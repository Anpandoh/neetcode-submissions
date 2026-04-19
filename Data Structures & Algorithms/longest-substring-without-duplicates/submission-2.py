class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l , r = 0 , 0
        longestSubstring = 0
        if len(s) == 1:
            return 1
        while r <  len(s):
            while s[l:r + 1].count(s[r]) > 1:
                l += 1
            longestSubstring = max(longestSubstring,  r - l + 1)
            r += 1


        return longestSubstring