#  File: MagicSquare.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic(a):
    n = int(len(a) ** (1 / 2))
    magic_number = int(n * (n ** 2 + 1) / 2)
    diagonal_sum = 0
    anti_diagonal_sum = 0
    b = [[a[row * n + i] for i in range(n)] for row in range(n)]
    for i, row in enumerate(b):
        if sum(row) != magic_number:
            return False
        if sum(b[col][i] for col in range(n)) != magic_number:
            return False
        diagonal_sum += b[i][i]
        for col in range(n):
            if (n - 1) - i == col:
                anti_diagonal_sum += b[i][col]
    if diagonal_sum != magic_number or anti_diagonal_sum != magic_number:
        return False
    return True


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute(a, idx, all_magic):
    hi = len(a)
    n = int(hi ** (1 / 2))
    magic_number = int(n * (n ** 2 + 1) / 2)
    if idx == hi:
        if is_magic(a):
            print(a)
    else:
        for i in range(1, n):
            if idx >= i * n:
                if sum(a[((i - 1) * n):(i * n)]) != magic_number:
                    return
            else:
                break
        for i in range(idx, hi):
            a[idx], a[i] = a[i], a[idx]
            permute(a, idx + 1, all_magic)
            a[idx], a[i] = a[i], a[idx]


def main():
    # read the dimension of the magic square
    in_file = open('magic.in', 'r')
    line = in_file.readline()
    line = line.strip()
    n = int(line)
    in_file.close()

    # create an empty list for all magic squares
    all_magic = []

    # create the 1-D list that has the numbers 1 through n^2
    nums = [num + 1 for num in range(n ** 2)]
    # generate all magic squares using permutation
    permute(nums, 0, all_magic)
    # print all magic squares


if __name__ == "__main__":
    main()
