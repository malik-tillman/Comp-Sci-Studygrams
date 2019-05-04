# Program to print an (n x n) symmetrical pascal matrix
# By: Malik Tillman
from pprint import pprint


def pascal_sym(n):
    """" Creates a n x n symmetrical pascal matrix """
    matrix = [[1] * n for _ in range(n)]  # Initialize n x n matrix of 1s

    for row in range(1, n):
        """" Loops n rows"""
        for col in range(1, n):
            """" Loops n columns"""
            matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]  # Calculates A(r,c) -> A(r-1,c) + A[r][c-1]

    return matrix


pprint([[0] * 10 for _ in range(10)])
