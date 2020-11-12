#  File: Chess.py

#  Description:

#  Student Name: Gabriel Mount

#  Student UT EID: gmm2767

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified: 10/23/2020

import sys

CT = 0


class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    def check_queens(self):
        num_queens = 0
        for row in self.board:
            for i in row:
                if i == 'Q':
                    num_queens += 1
        return num_queens

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do the recursive backtracking
    def recursive_solve(self, col):
        global CT
        if col == self.n and self.check_queens() == self.n:
            CT += 1
        elif col == self.n:
            return
        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    if self.recursive_solve(col + 1):
                        continue
                    self.board[i][col] = '*'

    # if the problem has a solution print the board
    def solve(self):
        for i in range(self.n):
            self.recursive_solve(i)


def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions
    game.solve()
    # print the number of solutions
    print(CT)


if __name__ == "__main__":
    main()
