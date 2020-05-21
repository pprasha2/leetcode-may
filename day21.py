'''
Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            matrix[i][0] = matrix[i-1][0] + matrix[i][0]
        for j in range(1,n):
            matrix[0][j] = matrix[0][j] + matrix[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1] + matrix[i][j] - matrix[i-1][j-1]
        print(matrix)
        dimension = min(m,n) + 1
        count = matrix[m-1][n-1]
        #print(count)
        for i in range(m):
            for j in range(n):
                isSquare = True
                for k in range(2,dimension):
                    if i + k > m or j + k > n or isSquare is False:
                        break
                    sq_count = k * k
                    compare = matrix[i+k-1][j+k-1]
                    if compare < sq_count:
                        continue
                    if j-1 >= 0:
                        compare -= matrix[i+k-1][j-1]
                    if i-1 >= 0:
                        compare -= matrix[i-1][j+k-1]
                        if j-1 >=0:
                            compare += matrix[i-1][j-1]
                    if compare == sq_count:
                        count += 1
                    else:
                        isSquare = False
        return count

