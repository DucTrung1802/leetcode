class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        i = 0
        raw_string = ""
        number = ""
        open_brackets = 0
        
        while i < len(s) and s[i].isalpha():
            raw_string += s[i]
            i += 1
        
        while i < len(s) and s[i].isdigit():
            number += s[i]
            i += 1
        
        if len(number) > 0:    
            k = int(number)
        
            open_brackets += 1
            i += 1
            open_char = i
            
            while open_brackets != 0:
                if s[i] == "[":
                    open_brackets += 1
                elif s[i] == "]":
                    open_brackets -= 1
                i += 1
                
            close_char = i - 1
        
            return raw_string + k * self.decodeString(s[open_char:close_char]) + self.decodeString(s[i:len(s)])
    
        else:
            return raw_string
    
hello = Solution()
print(hello.decodeString("abc5[e4[f]]4[k]"))

