class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_1 = {} # Dict for the first word
        word_2 = {} # Dict for the second word

        for letter in s:
            if letter not in word_1:
                word_1[letter] = 0
            word_1[letter] += 1

        for letter in t:
            if letter not in word_2:
                word_2[letter] = 0
            word_2[letter] += 1 

        return word_1 == word_2
        