from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0], reverse=False)
        
        res = []
        curr_arr = intervals[0]
        res.append(curr_arr)
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            curr_start = curr_arr[0]
            curr_end = curr_arr[1]
            
            next_start = interval[0]
            next_end = interval[1]
            
            if curr_end >= next_start:
                curr_arr[0] = min(curr_start, next_start)
                curr_arr[1] = max(curr_end, next_end)
            else:
                curr_arr = interval
                res.append(curr_arr)
                
        return res