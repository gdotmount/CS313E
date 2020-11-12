# File: Fibonacci.py

# Description:

# Student's Name: Gabriel Mount

# Student's UT EID: gmm2767

# Partner's Name:

# Partner's UT EID:

# Course Name: CS 313E

# Unique Number:

# Date Created: 10/09/2020

# Date Last Modified: 10/09/2020

import sys


memo = {}


def f(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        if n - 1 not in memo:
            memo[n - 1] = f(n - 1)
        if n - 2 not in memo:
            memo[n - 2] = f(n - 2)
        return memo[n - 1] + memo[n - 2]


# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap(s, p):
    occurrences = 0
    while len(s) >= len(p):
        if s[:len(p)] == p:
            occurrences = occurrences + 1
        s = s[1:]
    return occurrences


def main():
    # read n and p from standard input
    n = sys.stdin.readline()
    n = int(n.strip())
    p = sys.stdin.readline()
    p = p.strip()
    s = f(n)
    occ = count_overlap(s, p)
    print(occ)


if __name__ == "__main__":
    main()
