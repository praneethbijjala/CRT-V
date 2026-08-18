#1480. Running Sum of 1d Array
from ast import List


def runningSum(nums):
    res = [0] * (len(nums))
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(0, i + 1):
            curr_sum += nums[j]
        res[i] = curr_sum
    return res
    #optimal solution
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

#1732. Find the Highest Altitude
def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        alt = [0] * (n+1)
        for i in range(1,n+1):
            alt[i] = alt[i-1] + gain[i-1]
        return max(alt)