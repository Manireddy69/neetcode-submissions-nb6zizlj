# from _typeshed import StrOrBytesPath
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = s1.lower()
        s2 = s2.lower()
        len_s1 = len(s1)
        l = 0
        h = len_s1
        while h <= len(s2):
            if sorted(s2[l:h]) == sorted(s1):
                return True
            l += 1
            h += 1
        return False 