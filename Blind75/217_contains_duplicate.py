from operator import truediv
from typing import List

# O(n)
def containsDuplicate(nums: List[int]) -> bool:
    tracker = dict()

    for num in nums:
      if num in tracker:
        return True
      tracker[num] = True

    return False

print(containsDuplicate([1,1,1,3,3,4,3,2]))