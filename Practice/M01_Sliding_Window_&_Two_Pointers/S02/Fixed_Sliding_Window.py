#643.Maximum Subarray Average I
from ast import List
def findMaxAverage(nums: List[int], k: int) -> float:
    max_sum = sum(nums[:k])
    current_sum = max_sum

    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum / k
#1343. Number of Sub-arrays of Size K and Average Greater Than or Equal to Threshold
def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    count = 0
    current_sum = sum(arr[:k])
    if current_sum / k >= threshold:
        count += 1

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        if current_sum / k >= threshold:
            count += 1

    return count