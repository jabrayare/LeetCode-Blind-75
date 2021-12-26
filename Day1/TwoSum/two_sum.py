from typing import List

def twoSum(nums: List[int], target: int):
   # brute force solution
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
    return
    """
    # optimized solution.
    """
    We need to use a hashmap to keep track of numbers we have seen so far.
    """
    map = {}
    for i, num in enumerate(nums):
        res = target - num        
        if res in map:
            return [map[res], i]    
        else:
            map[num] = i
    return
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

      