class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).strip(' ').lower()
        return (s == s[::-1])