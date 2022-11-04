from collections import deque
from copy import deepcopy


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        while i+1 < len(nums):
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                del nums[i+1]
            
            i+=1
        
        return len(nums)

S = Solution()
TC = [1,1,2,2,3,4,5]
k = S.removeDuplicates(TC)
print(TC)
print(k)