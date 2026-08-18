#3.Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s: str) -> int:
        left = 0
        max_len = 0
        char_index_map = {}

        for right in range(len(s)):
            if s[right] in char_index_map and char_index_map[s[right]] >= left:
                left = char_index_map[s[right]] + 1

            char_index_map[s[right]] = right
            max_len = max(max_len, right - left + 1)

        return max_len
#424. Longest Repeating Character Replacement
def characterReplacement(s: str, k: int) -> int:
        left = 0
        max_len = 0
        char_count = {}
        max_count = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_count = max(max_count, char_count[s[right]])

            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len