class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        res = set()
        for i , num in enumerate(sorted_nums):
            target = 0-num
            l = i+1
            r  = len(sorted_nums) -1
            print(num)
            while l<r:
                sum_pair = sorted_nums[l] + sorted_nums[r]
                if sum_pair<target or l==i:
                    l+=1
                    continue
                if sum_pair>target or r==i:
                    r-=1
                    continue
                if sum_pair == target:
                    res.add((sorted_nums[i],sorted_nums[l],sorted_nums[r]))
                    l+=1
                    r-=1


        return list(res)


                
        