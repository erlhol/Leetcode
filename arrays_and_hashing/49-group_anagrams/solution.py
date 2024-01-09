from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strs:
            sorted_s = str(sorted(s))
            mapping[sorted_s].append(s)

        output = [x for x in mapping.values()]
        return output
