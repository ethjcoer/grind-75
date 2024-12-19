class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # This function determines if `ransomNote` can be constructed using
        # the letters in `magazine`. Each letter in `magazine` can only be
        # used once.

        letters = Counter(magazine)  # Count occurrences of each letter in magazine.

        for i in ransomNote:
            # Check if the current letter exists in `letters`.
            if i not in letters:
                return False  # If not, construction is impossible.

            # If the letter count is 1, remove it from the Counter.
            elif letters[i] == 1:
                del letters[i]
            else:
                # Otherwise, decrement the count of the letter.
                letters[i] -= 1

        return True  # If all letters are accounted for, return True.
