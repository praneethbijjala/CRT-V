#930.Binary Subarrays With Sum
from ast import List
def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    prefix_counts = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
      current_sum += num
      count += prefix_counts.get(current_sum - goal, 0)
      prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count

#1248. Count Number of Nice Subarrays
def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def sub_arr(target):
            if target < 0:
                return 0
            left,count,odd = 0,0,0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1
                while odd > target:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1
                count += (right-left+1)
            return count
        return sub_arr(k) - sub_arr(k-1)

