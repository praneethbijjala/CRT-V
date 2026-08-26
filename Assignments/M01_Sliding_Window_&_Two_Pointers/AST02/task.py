#Tasks
def Check_Palindrome(n: int, s: str) -> bool:
    def is_palindrome(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, n - 1

    while left < right:
        if s[left] != s[right]:
            return (
                is_palindrome(left + 1, right)
                or is_palindrome(left, right - 1)
            )
        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(Check_Palindrome(n, s))