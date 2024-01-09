class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.s_to_dict(s) == self.s_to_dict(t)

    def s_to_dict(self, s):
        return {i: s.count(i) for i in s}
