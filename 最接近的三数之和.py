class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0
        dis = float('inf')
        nums.sort()
        n = len(nums)
        for first in range(n):
            if first > 0 and nums[first - 1] == nums[first]:
                continue
            second = first + 1
            third = n - 1
            while second < third:
                if nums[second] + nums[third] == target - nums[first]:
                    return nums[first] + nums[second] + nums[third]
                elif nums[second] + nums[third] > target - nums[first]:
                    nowdis = abs(nums[first] + nums[second] + nums[third] - target)
                    if nowdis < dis:
                        dis = nowdis
                        ans = nums[first] + nums[second] + nums[third]
                    third -= 1
                else:
                    nowdis = abs(nums[first] + nums[second] + nums[third] - target)
                    if nowdis < dis:
                        dis = nowdis
                        ans = nums[first] + nums[second] + nums[third]
                    second += 1
        return ans
