class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        greatest = 0
        count = 0
        for num in nums:
            if (num == 1):
                count += 1
                greatest = max(count, greatest)
            else:
                count = 0
        return greatest