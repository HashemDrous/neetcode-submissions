class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counter = dict.fromkeys(nums, 0)
        for num in nums:
            if num in counter:
                counter[num] += 1
        
        for count in counter:
            if counter[count] > 1:
                return True
        
        return False