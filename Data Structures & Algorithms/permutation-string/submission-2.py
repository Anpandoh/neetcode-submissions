class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l , r = 0 , len(s1)
        s1 = sorted(s1)
        while r <= len(s2):
            s2substring = s2[l:r]
            print(s2substring)
            s2substring = sorted(s2substring)
            if s2substring == s1:
                return True
            l += 1
            r += 1
        
        return False


        