'''
input : 12,45,36,89,75,63,20
output: 12,36,20
'''
arr = list(map(int, input().split()))
i = 0

for j in range(len(arr)):
    if arr[j] % 2 == 0:
        arr[i] = arr[j]
        i += 1
print(arr[:i])