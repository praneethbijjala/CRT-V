def pairInSortedRotated(arr, target):
    n = len(arr)

    if n < 2:
        return False

    smallest = 0
    for i in range(1, n):
        if arr[i] < arr[smallest]:
            smallest = i

    low = smallest
    high = (smallest - 1 + n) % n

    while low != high:
        current_sum = arr[low] + arr[high]

        if current_sum == target:
            return True
        elif current_sum < target:
            low = (low + 1) % n
        else:
            high = (high - 1 + n) % n

    return False


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    target = int(input())
    print(pairInSortedRotated(arr, target))