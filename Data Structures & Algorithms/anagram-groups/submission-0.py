class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            key = ''.join(sorted(s))
            map.setdefault(key, []).append(s)
        return list(map.values())