# Program to reinforce my knowledge of matrix multiplication
# By: Malik Tillman

# Test case
rm = [[1, 7], [2, 4]]  # Matrix That Keeps Rows
cm = [[3, 3], [5, 2]]  # Matrix That Keeps Columns

# Get Matrices Columns and Rows
m1_cols = rm[0].__len__()
m1_rows = rm.__len__()
m2_cols = cm[0].__len__()
m2_rows = cm.__len__()


# Calculate 2 x 2 Matrix multiplication
def mult_matrix(a, b):
    """" Multiply Two 2 x 2 Matrices """
    dm = [[0, 0], [0, 0]]

    for r in range(2):
        for c in range(2):
            """" Dot Product Formula for 2 x 2 Matrix Multiplication"""
            dm[r][c] = (a[r][0] * b[0][c]) + (a[r][1] * b[1][c])

    return dm


# Get Matrices Multiplied
matrix = mult_matrix(rm, cm)
for i in range(matrix.__len__()):
    """" Print Results """
    print(str(matrix[i][0]) + " " + str(matrix[i][1]))
