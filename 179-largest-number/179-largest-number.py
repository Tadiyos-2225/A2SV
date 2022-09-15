class LargerNumKey(str):
     def __lt__(x, y):
        return x+y > y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            str1=""
            result=str1.join(sorted(map(str, nums),key=LargerNumKey))
            return '0' if result[0]=='0' else result
        
        
            