from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(lambda: [])

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            groups[tuple(count)].append(string)


        
        print(groups)
        return list(groups.values())