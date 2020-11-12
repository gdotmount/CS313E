def read_input():
    # open file for reading
    in_file = open('word.in', 'r')
    # read m and n
    coords = in_file.readline().strip().split()
    m = int(coords[0])
    n = int(coords[1])

    # skip blank line
    in_file.readline()

    # read the grid of characters
    word_grid = []
    for _ in range(m):
        word_grid.append(list(map(lambda x: x[0], in_file.readline().rstrip().split())))

    # skip blank line
    in_file.readline()
    k = int(in_file.readline().strip())

    # read the list of words
    word_list = []
    for _ in range(k):
        word_list_item = in_file.readline().strip()
        word_list.append(word_list_item)

    # close the input file
    in_file.close()

    return word_grid, word_list


def main():
    # read input from file
    word_grid, word_list = read_input()

    # call word_search() using the word_grid and word_list parameters
    for word in word_list:
        word_coordinates = word_search(word_grid, word)
        print(str(word_coordinates[0]) + " " + str(word_coordinates[1]))


def first_char (word_grid, word_to_search):
    char01_exists = False
    results = []
    char01 = word_to_search[0]
    for row_i, row in enumerate(word_grid):
        for col_i, colchar in enumerate(row):
            if char01 == colchar:
                char01_exists = True
                results.append(tuple((row_i, col_i)))
    return results, char01_exists


def word_search (word_grid, word_to_search):
    results, char01_exists = first_char(word_grid, word_to_search)

    if not char01_exists:
        return -1, -1

    word_to_search = word_to_search[1:]
    for result in results:
        row_i = result[0]
        col_i = result[1]
        if len(word_to_search) == 0:
            return result

        # search vertically downwards
        if len(word_grid) - (row_i + 1) >= len(word_to_search):
            exists = True
            i = row_i + 1
            for char in word_to_search:
                if char != word_grid[i][col_i]:
                    exists = False
                    break
                i += 1
            if exists:
                return result

        # search vertically upwards
        if row_i + 1 >= len(word_to_search):
            exists = True
            i = row_i - 1
            for char in word_to_search:
                if char != word_grid[i][col_i]:
                    exists = False
                    break
                i -= 1
            if exists:
                return result

        # search horizontally right
        if len(word_grid[row_i]) - (col_i + 1) >= len(word_to_search):
            exists = True
            i = col_i + 1
            for char in word_to_search:
                if char != word_grid[row_i][i]:
                    exists = False
                    break
                i += 1
            if exists:
                return result

        # search horizontally left
        if col_i + 1 >= len(word_to_search):
            exists = True
            i = col_i - 1
            for char in word_to_search:
                if char != word_grid[row_i][i]:
                    exists = False
                    break
                i -= 1
            if exists:
                return result

        # search diagonally up and to the right
        if (row_i + 1 >= len(word_to_search)
               and len(word_grid[row_i]) - (col_i + 1) >= len(word_to_search)):
            exists = True
            x = col_i + 1
            y = row_i - 1
            for char in word_to_search:
                if char != word_grid[y][x]:
                    exists = False
                    break
                x += 1
                y -= 1
            if exists:
                return result

        # search diagonally down and to the right
        if (len(word_grid) - (row_i + 1) >= len(word_to_search)
               and len(word_grid[row_i]) - (col_i + 1) >= len(word_to_search)):
            exists = True
            x = col_i + 1
            y = row_i + 1
            for char in word_to_search:
                if char != word_grid[y][x]:
                    exists = False
                    break
                x += 1
                y += 1
            if exists:
                return result

        # search diagonally up and to the left
        if (row_i + 1 >= len(word_to_search)
               and col_i + 1 >= len(word_to_search)):
            exists = True
            x = col_i - 1
            y = row_i - 1
            for char in word_to_search:
                if char != word_grid[y][x]:
                    exists = False
                    break
                x -= 1
                y -= 1
            if exists:
                return result

        # search diagonally down and to the left
        if (len(word_grid) - (row_i + 1) >= len(word_to_search)
               and col_i + 1 >= len(word_to_search)):
            exists = True
            x = col_i - 1
            y = row_i + 1
            for char in word_to_search:
                if char != word_grid[y][x]:
                    exists = False
                    break
                x -= 1
                y += 1
            if exists:
                return result

    return -1, -1


main()
