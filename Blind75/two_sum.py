from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
      for j in range(len(nums)):
          if i != j and nums[i] + nums[j] == target:
              return [i, j]

print(twoSum([1, 2, 3, 4, 5], 6))