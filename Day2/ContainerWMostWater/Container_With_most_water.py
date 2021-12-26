from typing import List
def maxArea(height: List[int]) -> int:
  left, right = 0, len(height) -1
  largest_area = 0
  
  while left < right:
    area = abs(right - left) * min(height[left], height[right])
    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
    largest_area = max(largest_area, area)
  return largest_area
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))