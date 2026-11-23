class Solution:
    def isPalindrome(self, s: str) -> bool:
        # IDEA: Read the string from both right and left side. If the word is a palindrome, each pointer would have the same current character.

        # 1. Clean and prepare the string with only alphanumerical characters
        clean = "".join(ch.lower() for ch in s if ch.isalnum())

        L = 0                   # Index starting from the first character
        R = len(clean) - 1      # Index starting from the last character

        while L < R:
            if clean[L] != clean[R]:
                return False
            L += 1
            R -= 1

        return True