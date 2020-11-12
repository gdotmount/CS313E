#  File: Triangle.py

#  Description: Let's freaking go

#  Student Name: Gabriel Maximus Mount

#  Student UT EID: GMM2767

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 50845

#  Date Created: 10/26/2020

#  Date Last Modified: 10/26/2020

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force(grid):
    paths = []
    brute_solve(grid, paths)
    return max(paths)


def brute_solve(grid, paths, row=0, i=0, summer=0):
    summer += grid[row][i]
    n = len(grid) - 1
    if row == n:
        paths.append(summer)
    else:
        brute_solve(grid, paths, row + 1, i, summer)
        brute_solve(grid, paths, row + 1, i + 1, summer)


# returns the greatest path sum using greedy approach
def greedy(grid):
    j = 0
    max_sum = 0
    n = len(grid) - 1
    for ind, row in enumerate(grid):
        max_sum += row[j]
        if ind < n:
            left = grid[ind + 1][j]
            right = grid[ind + 1][j + 1]
            if right > left:
                j += 1
    return max_sum


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    return recursive_solve(grid)


def recursive_solve(grid, row=0, i=0):
    n = len(grid) - 1
    if row == n:
        return grid[row][i]
    else:
        return grid[row][i] + max(recursive_solve(grid, row + 1, i), recursive_solve(grid, row + 1, i + 1))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    grid.reverse()
    a = grid[:]
    for i in range(1, len(grid)):
        for j, el in enumerate(grid[i]):
            if el != 0:
                left = grid[i - 1][j]
                right = grid[i - 1][j + 1]
                if right > left:
                    a[i][j] = a[i][j] + right
                else:
                    a[i][j] = a[i][j] + left
            else:
                break
    return a[-1][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    print('The greatest path sum through exhaustive search is', brute_force(grid), sep='\n')
    print('The time taken for exhaustive search in seconds is', times, '', sep='\n')
    # print time taken using exhaustive search

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    print('The greatest path sum through greedy search is', greedy(grid), sep='\n')
    print('The time taken for greedy search in seconds is', times, '', sep='\n')
    # print time taken using greedy approach

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    print('The greatest path sum through divide and conquer search is', divide_conquer(grid), sep='\n')
    print('The time taken for divide and conquer search in seconds is', times, '', sep='\n')
    # print time taken using divide-and-conquer approach

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    print('The greatest path sum through dynamic programming is', dynamic_prog(grid), sep='\n')
    print('The time taken for dynamic programming in seconds is', times, '', sep='\n')
    # print time taken using dynamic programming


if __name__ == "__main__":
    main()
