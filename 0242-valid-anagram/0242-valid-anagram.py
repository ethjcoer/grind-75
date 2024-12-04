class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(N log N) solution.
        #
        # Strings are a sequence of unicode characters.
        # At least in Python, they can be sorted.
        # return sorted(s) == sorted(t)

        # O(N) solution.
        #
        # Two words with different lengths can't be anagrams.
        if len(s) != len(t):
            return False

        # Utilize hashmaps to compare them in O(N) time.
        hashmapS = {}
        hashmapT = {}

        # Iterate over both strings simultaneously.
        for _s, _t in zip(s, t):
            # The hashmaps are populated with characters as keys and their
            # number of instances as values.
            hashmapS[_s] = 1 + hashmapS.get(_s, 0)
            hashmapT[_t] = 1 + hashmapT.get(_t, 0)

        # Compare the two hashmaps to check if the strings are anagrams.
        return hashmapS == hashmapT
