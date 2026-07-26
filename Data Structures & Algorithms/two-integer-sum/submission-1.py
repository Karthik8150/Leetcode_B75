class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #3:0
        #4:1
        #3 in hashmap.keys

        for i,num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[num] = i
