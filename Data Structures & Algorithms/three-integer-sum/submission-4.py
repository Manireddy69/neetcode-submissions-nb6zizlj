class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            target = -nums[i]
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    result.append([nums[i], nums[l], nums[r]])
                    ## handle left pointer duplicates
                    while l < r and nums[l] == nums[l+1]:
                        l +=1 
                    ## handle right pointer duplicates
                    while l < r and nums[l] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    r-= 1
        return result
