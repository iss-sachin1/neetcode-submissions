class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        
        for word in strs:
            s += (str(len(word)) + "#" + word) 
        
        return s

    def decode(self, s: str) -> List[str]:
        rList = []
        while len(s) > 0:
            start = 0
            end = 0

            start = s.index("#") + 1
            end = int(s[0:start-1]) + start

            rList.append(s[start:end])
            s = s.replace(s[0:end], "", 1)


            
        return rList

        

        






