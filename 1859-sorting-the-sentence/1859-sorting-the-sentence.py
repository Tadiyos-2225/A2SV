class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        result = []
        for word in arr:
            position = word[-1]
            word = word[:-1]
            result.append((position, word))
            # print(position)
        # print(arr)
        result.sort()
        ans = ""
        for x  in result:
            ans = ans + x[1] + " "
        return ans.strip()
      
          
          
        
                  