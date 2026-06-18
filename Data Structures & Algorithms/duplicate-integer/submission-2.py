class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences  = defaultdict(int)
        for num in nums:
            occurences[num]+=1
            if occurences[num] > 1:
                return True
        return False