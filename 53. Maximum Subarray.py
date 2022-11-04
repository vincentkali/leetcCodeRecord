# [-2,1,-3,4,-1,2,1,-5,4]
# [-2,-1]
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

TC = [-10000] * 10000
S = Solution()
result = S.maxSubArray(TC)
print(result)