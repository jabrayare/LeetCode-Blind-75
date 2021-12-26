from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort(key=None, reverse=False)
    res = []
    
    for i in range(len(nums)-2):
      num = nums[i]
      left, right = i + 1, len(nums) -1
      
      while left < right:
        if nums[left] + nums[right] + num == 0:
          if [num,nums[left], nums[right]] not in res:
              res.append([num,nums[left], nums[right]])
          left += 1
          right -= 1
        elif nums[left] + nums[right] + num < 0:
          left += 1
        else: 
          right -= 1
    return res
nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(threeSum(nums))