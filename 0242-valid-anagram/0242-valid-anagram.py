class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings are a sequence of unicode characters.
        # At least in Python, they can be sorted.
        return sorted(s) == sorted(t)
