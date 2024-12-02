class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Based on Codebagel's solution: https://youtu.be/7gWFRA0V0OE?t=264
        # Initialize an empty string 'word' to store the alphanumeric characters
        # in lowercase.
        word = ""

        # Iterate over each character in the input string 's'.
        for _ in s:
            # Check if the current character is alphanumeric (a letter or a number).
            # If it is, convert it to lowercase and add it to the 'word' string.
            if _.isalnum():
                word += _.lower()

        # Return True if 'word' is equal to its reverse, indicating it's a palindrome.
        return word == word[::-1]
