#!/usr/bin/python3
"""
Test 0x16 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Original matrix: ")
    print(matrix)
    rotate_2d_matrix(matrix)
    print("Rotated matrix: ")
    print(matrix)
    matrix = [[1, 2, 3, 4],
              [10, 20, 30, 40],
              [100, 200, 300, 400],
              [1000, 2000, 3000, 4000]]
    print("Original matrix: ")
    print(matrix)
    rotate_2d_matrix(matrix)
    print("Rotated matrix: ")
    print(matrix)
