class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_list=[]
        result=[]
        for x in nums:
            for y in nums:
                if x > y:
                    new_list.append(y)
            size=len(new_list)
            result.append(size)
            new_list.clear()
        return result
     
          
            
            
        