class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        size = len(nums)

        for i in range(0, size):
            find_complement = target - nums[i]
            if find_complement in hashmap:
                return [hashmap[find_complement], i]

            hashmap[nums[i]] = i
             
        return []

