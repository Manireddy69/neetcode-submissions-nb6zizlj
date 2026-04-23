class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        for num in nums[1:]:
            c = (num , num*max_prod, num*min_prod)
            max_prod = max(c)
            min_prod = min(c)
            result = max(result, max_prod)
        return result