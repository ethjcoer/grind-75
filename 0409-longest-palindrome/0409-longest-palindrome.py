class Solution:
    def longestPalindrome(self, s: str) -> int:
        # This function computes the length of the longest palindrome
        # that can be built using the characters in the string `s`.

        length = 0  # Tracks the length of the palindrome being built.
        chars = set()  # Stores characters with an odd frequency.

        for i in s:
            if i in chars:
                # If the character is already in the set, it forms a pair.
                chars.remove(i)  # Remove the paired character.
                length += 2  # Add 2 to the palindrome length for the pair.
            else:
                # If the character isn't in the set, add it.
                chars.add(i)

        # If any characters remain in the set, one can be used as the center.
        return length + 1 if chars else length
