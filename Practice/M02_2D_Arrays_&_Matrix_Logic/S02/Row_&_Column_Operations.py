
#1351.Count Negative Numbers in a sorted matrix
from typing import List
import typing


def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        count = 0
        for row in grid:
            for ele in row:
                if ele < 0:
                    count += 1
        return count
        '''
#832.Flipping an Image
def flipAndInvertImage(self, image: List[List[int]]) -> List[typing.List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image

