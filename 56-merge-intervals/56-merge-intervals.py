class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals = sorted(intervals, key=lambda x: x[0])
        new_interval=intervals[0]
        for x in range(1,len(intervals)):
            if new_interval[1] >= intervals[x][0]:
                new_interval=[min(new_interval[0],intervals[x][0]),max(new_interval[1],intervals[x][1])]
            
            else:
                res.append(new_interval)
                new_interval=[intervals[x][0],intervals[x][1]]
        res.append(new_interval)
        return res