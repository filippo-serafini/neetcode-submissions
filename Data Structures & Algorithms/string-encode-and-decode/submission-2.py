class Solution:
    # Pro Solution: we encode using the length of each string, followed by a # as to say "the end of the number length" and "this is the beginning of the word"

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            w_len = len(word)
            result += str(w_len) + '#' + word
        
        return result

    def decode(self, s: str) -> List[str]:
        result = [] # String array
        i = 0

        temp_length = ""
        length = 0

        while i < len(s):
            

            # 1. Read the word length
            while s[i] != '#':
                temp_length += s[i]
                i += 1    
            
            # Convert the lenght str to a number
            length = int(temp_length)

            i += 1 # Skip the #
            result.append(s[i: i + length]) # i as the offset
            i += length
            temp_length = ""
            
        return result