
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        i = 0
        while i < len(nums):
            j = i + 1  # start j from the next index
            while j < len(nums):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
                j += 1
            i += 1
        return False
