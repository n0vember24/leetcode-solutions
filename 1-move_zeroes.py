# https://leetcode.com/problems/move-zeroes/description/

# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

from typing import List


class Solution:
	def moveZero(self, nums: List[int]) -> List:
		lastNonZeroFoundAt = 0
		for cur in range(len(nums)):
			if nums[cur] != 0:
				nums[lastNonZeroFoundAt], nums[cur] =  nums[cur], nums[lastNonZeroFoundAt]
				lastNonZeroFoundAt += 1

		return nums

inp =  [0, 1, 0, 3, 0, 14, 33, 35, 77, 0, 13, 0, 0, 0, 232, 345, 5, 0, 12]
solution = Solution()
out = solution.moveZero(inp)
print(out)
