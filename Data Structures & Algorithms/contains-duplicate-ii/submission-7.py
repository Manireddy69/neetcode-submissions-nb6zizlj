class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return abs(i -j) <= k
        # return False

        for i in range(len(nums)):  # fix: removed -1
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
                    # abs(i - j) <= k
        return False
