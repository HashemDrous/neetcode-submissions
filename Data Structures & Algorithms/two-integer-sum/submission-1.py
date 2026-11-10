class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # 3: 0, 4: 1, 5: 2, 6: 3}

        # Determine complement

        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]
            
            seen[num] = index
        



        