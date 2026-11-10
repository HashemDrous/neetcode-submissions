class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Make a dict counter
        counter = {}

        for num in nums:
            
            # Return false if any counter is greater than 1
            if num in counter:
                return True
            else:
                counter[num] = 1
        
        return False
        