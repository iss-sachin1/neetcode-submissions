class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rList = []
        original = list(strs)

        for i, str in enumerate(strs):
            strs[i] = "".join(sorted(str))
        


        s = set(strs)
        hashmap = {item: [] for item in s}

        for i, word in enumerate(strs):
            hashmap[word].append(original[i]) 
        
        for word in hashmap:
            rList.append(hashmap[word])

        return rList
            


     
        

            


            
        