class Solution:
    def sortColors(self, nums: List[int]) -> None:
        result=[]
        nums.sort()
        for x in nums:
            for y in nums:
                if x < y:
                    result.append(x)
            return result
        """
        Do not return anything, modify nums in-place instead.
        """
        