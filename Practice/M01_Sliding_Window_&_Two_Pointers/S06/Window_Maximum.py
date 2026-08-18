#1763.Longest_Nice_Substring.py
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(substring):
            char_set = set(substring)
            for char in char_set:
                if char.islower() and char.upper() not in char_set:
                    return False
                if char.isupper() and char.lower() not in char_set:
                    return False
            return True

        max_length = 0
        longest_substring = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    longest_substring = substring

        return longest_substring

