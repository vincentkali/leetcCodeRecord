# [-2,1,-3,4,-1,2,1,-5,4]
# [-2,-1]
from functools import cache
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return nums[0]

        preSum = curSum = 0
        max_ = -1 * pow(10,5)
        for i in range(len(nums)):
            if nums[i] >= preSum and preSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]
            # max_ = max(max_, curSum)
            if curSum > max_:
                max_ = curSum
                # print(max_)
                # print(i)

            preSum = curSum
        
        return max_

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        len_ = len(nums)
        @cache
        def solve(i, must_pick):
            print(i, must_pick)
            if i >= len_: return 0 if must_pick else -100000000
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)


TC = [5,4,-1,7,8]
S = Solution()
result = S.maxSubArray(TC)
print(result)