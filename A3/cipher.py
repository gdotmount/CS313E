perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def gridify(g_str, mode='encrypt'):
    if not len(g_str) - 1:
        return [[g_str]]
    for i, square in enumerate(perfect_squares):
        if square < len(g_str) <= perfect_squares[i + 1]:
            break
    K = int(perfect_squares[i + 1] ** 0.5)
    diff = perfect_squares[i + 1] - len(g_str)
    grid = [[None] * K for _ in range(K)]
    if mode == 'decrypt':
        for ind in range(diff):
            grid[K - 1 - ind][0] = ''
    for row_ind, row in enumerate(grid):
        for ind, element in enumerate(row):
            if element is None:
                grid[row_ind][ind] = g_str[0] if len(g_str) else ''
                g_str = g_str[1:]
    [print(row) for row in grid]
    return grid


def stringify(grid):
    return ''.join(char for row in grid for char in row)


def encrypt(p_str):
    p_str = gridify(p_str)
    rotated_grid = [[None] * len(p_str) for _ in range(len(p_str))]
    for i, row in enumerate(p_str):
        col_i = len(p_str) - (1 + i)
        for ind, char in enumerate(row):
            rotated_grid[ind][col_i] = char

    return stringify(rotated_grid)


def decrypt(q_str):
    q_str = gridify(q_str, 'decrypt')
    rotated_grid = [[None] * len(q_str) for _ in range(len(q_str))]
    for i, row in enumerate(q_str):
        for ind, char in enumerate(row):
            row_i = len(q_str) - (ind + 1)
            rotated_grid[row_i][i] = char

    return stringify(rotated_grid)


def main():
    p = input()
    q = input()
    print(encrypt(p))
    print(decrypt(q))


if __name__ == "__main__":
  main()
