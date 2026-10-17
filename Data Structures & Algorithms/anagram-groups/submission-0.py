from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            count = {}
            for char in string:
                count[char] = count.get(char, 0) + 1
            key = tuple(sorted(count.items()))
            groups[key].append(string)
        return list(groups.values())