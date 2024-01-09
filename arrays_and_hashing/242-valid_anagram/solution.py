class Solution:
    # Solution approach:
    # 1. Create a hashmap (dictionary) for each of the words, s and t
    # 2. Check if the dictionaries are equal.

    # Time complexity: O(n)

    def isAnagram(self, s: str, t: str) -> bool:
        s_char_dict = self.create_map(s)
        t_char_dict = self.create_map(t)

        return s_char_dict == t_char_dict

    def create_map(self, s):
        char_dict = dict()
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        return char_dict
