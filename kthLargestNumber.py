class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = int, reverse = True)
        for i in range(len(nums)):
            if i==k-1:
                return str(nums[i])
                
           
