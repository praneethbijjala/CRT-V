#1493.Longest Subarray of 1's After Deleting One Element
def longestSubarray(nums: list[int]) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len - 1 if max_len > 0 else 0

#1004. Max Consecutive Ones III
def longestOnes(nums: list[int], k: int) -> int:
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len

#930. Binary Subarrays With Sum
def numSubarraysWithSum(nums: list[int], goal: int) -> int:
        left = 0
        current_sum = 0
        count = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > goal and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == goal:
                count += 1

        return count

#1358. Number of Substrings Containing All Three Characters
def numberOfSubstrings(s: str) -> int:
        left = 0
        count = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}

        for right in range(len(s)):
            char_count[s[right]] += 1

            while all(char_count[char] > 0 for char in char_count):
                count += len(s) - right
                char_count[s[left]] -= 1
                left += 1

        return count