from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)
        for c in s:
            hashMap[c] += 1
        for c in t:
            hashMap[c] -= 1
        return all(val == 0 for val in hashMap.values())

        