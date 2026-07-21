class Solution:
     def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for s in strs:
            
            encoded_string += f"{len(s)}#{s}"
        return encoded_string

    
     def decode(self, s: str) -> list[str]:
        result = []
        i = 0 

        while i < len(s):
            
            j = i
            while s[j] != '#':
                j += 1
              
            length = int(s[i:j])
            start_of_string = j + 1
            end_of_string = start_of_string + length
            result.append(s[start_of_string:end_of_string])
            i = end_of_string
            
        return result