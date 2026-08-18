#1652. Maximum in Each Subarray of Size k
def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    from collections import deque
    result = []
    window = deque()

    for i in range(len(nums)):
        # Remove elements that are out of the current window
        if window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements that are smaller than the current element
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        window.append(i)

        # Append the maximum for the current window
        if i >= k - 1:
            result.append(nums[window[0]])

    return result