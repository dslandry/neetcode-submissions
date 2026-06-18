class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [ [] for _ in range(len(nums)+1) ]
        count = defaultdict(int)

        for num in nums:
            count[num]+= 1
        
        for num, occurences in count.items():
            frequencies[occurences].append(num)
        
        res = []
        for i in range(len(frequencies)-1, 0, -1):
            for x in frequencies[i]:
                res.append(x)
            if len(res) ==k:
                return res

