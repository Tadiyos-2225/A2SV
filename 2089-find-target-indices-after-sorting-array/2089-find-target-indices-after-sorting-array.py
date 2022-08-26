class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result=[]
        for index, x in enumerate(nums, start=0):
            if x==target:
                result.append(index)
        return result