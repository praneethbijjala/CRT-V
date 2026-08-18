#leetcode problems
# no. 26. Remove Duplicates from Sorted Array
from typing import List
def removeDuplicates(nums: List[int]) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
#27.Remove Element
def removeElement(nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
#283. Move Zeroes
def moveZeroes(nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for k in range(i,len(nums)):
            nums[k] = 0
#167. Two Sum II - Input Array Is Sorted
def twoSum(numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left,right = 0,n-1
        while left<right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1,right+1]
            elif s > target:
                right -= 1
            else:
                left += 1
#977. Squares of a Sorted Array
def sortedSquares(nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        left,right = 0,n-1
        for i in range(n-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left]**2
                left += 1
            else:
                res[i] = nums[right]**2
                right -= 1
        return res
