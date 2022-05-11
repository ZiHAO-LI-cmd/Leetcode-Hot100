class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for first in range(len(nums) - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            for second in range(first + 1, len(nums) - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                third = second + 1
                fourth = len(nums) - 1
                while third < fourth:
                    total = nums[first] + nums[second] + \
                        nums[third] + nums[fourth]
                    if total == target:
                        res.append([nums[first], nums[second],
                                   nums[third], nums[fourth]])
                        while third < fourth and nums[third] == nums[third + 1]:
                            third += 1
                        third += 1
                        while third < fourth and nums[fourth] == nums[fourth - 1]:
                            fourth -= 1
                        fourth -= 1
                    elif total < target:
                        third += 1
                    else:
                        fourth -= 1
        return res
