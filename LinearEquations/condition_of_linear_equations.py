import numpy as np
from inverse_matrix import matrix_inverse
from matrix_utility import print_matrix


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    # Step 2: Calculate the inverse of A
    A_inv = matrix_inverse(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    print("A:")
    print_matrix(A)

    print("inverse of A:")
    print_matrix(A_inv)

    print("Max Norm of A:", norm_A, "\n")

    print("max norm of the inverse of A:", norm_A_inv)

    return cond


if __name__ == '__main__':
    A = np.array([[2, 1, 0],
           [3, -1, 0],
           [1, 4, -2]])
    cond = condition_number(A)

    print("\n condition number: ", cond)


    value = norm(A) + 4

    print("\n\n\nMax Norm of A:", norm(A), "\n")

    print("sum of  the norm of the coefficients matrix and the question number(4):", value)