from typing import List
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    self.transposeMatrix(matrix)
    self.reverse(matrix)
    
        
def transposeMatrix(self, matrix: List[List[int]]) -> None:
    rows = len(matrix)
    
    for i in range(rows):
        for j in range(i, rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
    
def reverse(self, matrix):
    for arr in matrix:
        start = 0
        end = len(arr) - 1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1