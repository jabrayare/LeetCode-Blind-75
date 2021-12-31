from typing import List

# Greedy Algorithm
class Solution:
  def canJump(self, nums: List[int]) -> bool:
      goal = len(nums) - 1
      
      for i in range(len(nums) -1, -1, -1):
          if i + nums[i] >= goal:
              goal = i
      return goal == 0

nums = [2,3,1,1,4]
solution = Solution()
print(solution.canJump(nums))
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
print(solution.canJump(nums))

