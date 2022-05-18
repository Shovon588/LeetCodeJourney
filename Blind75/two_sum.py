from typing import List

# O(n^2)
def twoSum(nums: List[int], target: int) -> List[int]:
  for i in range(len(nums)):
      for j in range(len(nums)):
          if i != j and nums[i] + nums[j] == target:
              return [i, j]

print(twoSum([1, 2, 3, 4, 5], 6))

# O(n)
def twoSum(nums: List[int], target: int) -> List[int]:
  hash_map = dict()
  for i in range(len(nums)):
    required = target - nums[i]
    if required in hash_map:
      return [i, hash_map[required]]

    hash_map[nums[i]] = i

print(twoSum([1, 2, 3, 4, 5], 6))
