class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        relative_map = {target-num : i for i, num in enumerate(nums) }
        
        for i, num in enumerate(nums):
            relative_index = relative_map.get(num)
            if relative_index is not None and relative_index !=i:
                return sorted([i,relative_index])
        