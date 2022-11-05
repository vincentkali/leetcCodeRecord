class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for e in nums:
            if e in s:
                return True
            s.add(e)
        return False