from typing import List
def The_Great_Run(N: int,k:int,arr:List[int]) -> int:
   current = sum(arr[:k])
   maximum = current

   for i in range(k, N):
        current += arr[i] - arr[i - k]
        maximum = max(maximum, current)

   return maximum

if __name__ == '__main__':
    N,k = map(int,input().split())
    path = list(map(int,input().split()))
    print(The_Great_Run(N,k,path))
