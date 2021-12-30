from typing import List
def maxSubArray(nums: List[int]) -> int:
    largest_sum = nums[0]
    current_sum = nums[0]
    
    for second in range(1, len(nums)):
        current_sum = max(current_sum + nums[second], nums[second])
        largest_sum = max(largest_sum, current_sum)
    return largest_sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
print(maxSubArray(nums))