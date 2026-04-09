class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        l = list(s.lower())
        for char in l:
            if char.isalnum():
                result.append(char)
        return result[:] == result [::-1]