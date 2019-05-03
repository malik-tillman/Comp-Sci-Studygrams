# Program to reinforce my knowledge of matrix multiplication
# By: Malik Tillman
from pprint import pprint as pp

# Test case
rm = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],
      [1, 4, 10, 20, 35, 56, 84, 120, 165, 220],
      [1, 5, 15, 35, 70, 126, 210, 330, 495, 715],
      [1, 6, 21, 56, 126, 252, 462, 792, 1287, 2002],
      [1, 7, 28, 84, 210, 462, 924, 1716, 3003, 5005],
      [1, 8, 36, 120, 330, 792, 1716, 3432, 6435, 11440],
      [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310],
      [1, 10, 55, 220, 715, 2002, 5005, 11440, 24310, 48620]]  # Matrix That Keeps Rows
cm = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],
      [1, 4, 10, 20, 35, 56, 84, 120, 165, 220],
      [1, 5, 15, 35, 70, 126, 210, 330, 495, 715],
      [1, 6, 21, 56, 126, 252, 462, 792, 1287, 2002],
      [1, 7, 28, 84, 210, 462, 924, 1716, 3003, 5005],
      [1, 8, 36, 120, 330, 792, 1716, 3432, 6435, 11440],
      [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310],
      [1, 10, 55, 220, 715, 2002, 5005, 11440, 24310, 48620]]  # Matrix That Keeps Columns
sz = 10


# Calculate 2 x 2 Matrix multiplication
def mult_matrix(m_plier, m_plicand):
    """" Multiply Two 2 x 2 Matrices """
    dm = [[1] * sz for _ in range(sz)]

    for r in range(len(m_plier)):
        """" Iterate through rows of multiplier """
        for c in range(len(m_plicand[0])):
            """" Iterate through columns of multiplicand """
            for r2 in range(len(m_plicand)):
                """" Iterate through rows of multiplicand """
                dm[r][c] += m_plier[r][c] * m_plicand[r2][c]  # Dot Product Formula for 2 x 2 Matrix Multiplication

    return dm


# Find dot product
pp(mult_matrix(rm, cm))
