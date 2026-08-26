def pairInSortedRotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    pivot = 0
    for i in range(1, n):
        if arr[i] < arr[pivot]:
            pivot = i

    low = pivot
    high = (pivot - 1 + n) % n

    while low != high:
        total = arr[low] + arr[high]

        if total == target:
            return True
        elif total < target:
            low = (low + 1) % n
        else:
            high = (high - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))