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
        for a, b in zip(s, t):
            # The hashmaps are populated with characters as keys and their
            # number of instances as values.
            hashmapS[a] = 1 if a not in hashmapS else hashmapS[a] + 1
            hashmapT[b] = 1 if b not in hashmapT else hashmapT[b] + 1

        # Compare the two hashmaps to check if the strings are anagrams.
        return hashmapS == hashmapT
