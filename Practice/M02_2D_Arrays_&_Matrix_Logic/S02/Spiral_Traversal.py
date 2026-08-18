def spiralOrder(matrix):
    rows,cols = len(matrix),len(matrix[0])
    
    top,bottom = 0,rows - 1
    left,right = 0,cols - 1

    ans = []

    while top <= bottom and left <= right:

        # left -> right
        for col in range(left, right + 1):
            ans.append(matrix[top][col])
        top += 1

        # top -> bottom
        for row in range(top, bottom + 1):
            ans.append(matrix[row][right])
        right -= 1

        # right -> left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                ans.append(matrix[bottom][col])
            bottom -= 1

        # bottom -> top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                ans.append(matrix[row][left])
            left += 1

    return ans
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))