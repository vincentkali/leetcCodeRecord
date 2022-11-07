class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_ = len(nums)
        pre = [1] * len_
        suf = [1] * len_
        ans = [1] * len_
        for i in range(0, len_):
            pre[i] = (pre[i-1] if i!=0 else 1) * nums[i]
        for i in range(len_-1,-1,-1):
            # print(i)
            suf[i] = (suf[i+1] if i!=len_-1 else 1) * nums[i]
        # print(pre)
        # print(suf)
        for i in range(len_):
            ans[i] = (pre[i-1] if i !=0 else 1) * (suf[i+1] if i!= len_-1 else 1)

        return ans            

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        len_ = len(nums)
        pre = suf = 1
        ans = [1] * len_
        for i in range(len_):
            ans[i] *= pre
            ans[-1-i] *= suf
            pre *= nums[i]
            suf *= nums[-1-i]
        return ans
        




        
testCase = [1,2,3,4]
S = Solution()
result = S.productExceptSelf(testCase)
print(result)


