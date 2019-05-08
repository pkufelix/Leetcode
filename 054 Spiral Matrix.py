"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        top = 0
        left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        while top < bottom and left < right:
            for i in range(left,right):
                res.append(matrix[top][i])
            for j in range(top,bottom):
                res.append(matrix[j][right])
            for i in range(right,left,-1):
                res.append(matrix[bottom][i])
            for j in range(bottom,top,-1):
                res.append(matrix[j][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right and top == bottom:
            res.append(matrix[top][left])
        if left == right and top != bottom:
            for j in range(top,bottom+1):
                res.append(matrix[j][left])
        if left != right and top == bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        return res