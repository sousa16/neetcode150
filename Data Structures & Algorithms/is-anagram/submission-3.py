from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)
        for c in s:
            hashMap[c] += 1
        for c in t:
            hashMap[c] -= 1
        return all(v == 0 for v in hashMap.values())