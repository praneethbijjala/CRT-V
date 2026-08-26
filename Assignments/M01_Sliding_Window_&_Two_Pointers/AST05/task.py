from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    left_product = 1
    for i in range(n):
        res[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]

    return res


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(productExceptSelf(arr))