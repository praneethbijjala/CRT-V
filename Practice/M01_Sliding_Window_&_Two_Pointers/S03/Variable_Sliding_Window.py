#209.Minimum size Subarray Sum
from ast import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
        left = 0
        min_len = float("inf")
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len,right-left+1)
                cur_sum -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len
#713. Subarray Product Less Than K
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            count += right - left + 1

        return count

#904. Fruit Into Baskets
def totalFruit(fruits: List[int]) -> int:
        left = 0
        max_len = 0
        fruit_count = {}

        for right in range(len(fruits)):
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1

            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len