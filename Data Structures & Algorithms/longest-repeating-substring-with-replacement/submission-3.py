from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charCount = defaultdict(lambda: 0)
        l = 0
        r = 0
        mostFreq = 0
        longestSubstring = 0
        while r < len(s):
            charCount[s[r]] += 1

            mostFreq = max(mostFreq, charCount[s[r]])

            if r - l - mostFreq + 1> k:
                charCount[s[l]] -= 1
                l += 1
            r += 1
        
        return len(s) - l


        #wrong
        # l , r = 0, 1
        # longestSubstring = 0
        # firstReplacement = 0
        # currK = k
        # while r < len(s):
        #     print(s[l], s[r])
        #     if s[r] != s[l]:                    
        #         if currK > 0:
        #             if currK == k:
        #                 firstReplacement = r
        #             currK -= 1
        #         else:
        #             if k == 0:
        #                  l = r
        #             else:
        #                 currK = k
        #                 l = firstReplacement
        #                 r = firstReplacement
        #     longestSubstring = max(longestSubstring, r - l + 1)
        #     r += 1

        # return longestSubstring
        