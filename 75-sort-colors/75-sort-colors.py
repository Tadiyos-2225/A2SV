class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # result=[]
        for i in range(len(nums)):
            for x in range(len(nums)-i-1):
                if nums[x] > nums[x+1]:
                    nums[x],nums[x+1]=nums[x+1],nums[x]
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        