def guaranteed_space(grid, office):
    guarspace = 0
    for row in range(office[2], office[4]):
        for space in range(office[1], office[3]):
            if grid[len(grid) - row - 1][space] == 1:
                guarspace += 1
    return guarspace


def contest_space(grid, offices):
    for office in offices:
        for row in range(office[2], office[4]):
            for space in range(office[1], office[3]):
                grid[len(grid) - row - 1][space] += 1
    return grid


def contested_space(grid):
    conspace = 0
    for row in grid:
        for space in row:
            if space > 1:
                conspace += 1
    return conspace


def unallocated_space(grid, offices):
    unallspace = 0
    for row in grid:
        for space in row:
            if space == 0:
                unallspace += 1
    return unallspace


def main():
    dimensions = input().split()
    width = int(dimensions[0])
    length = int(dimensions[1])
    grid = [[0] * (width) for _ in range(length)]
    num_offices = int(input())
    print(f'Total {width * length}')
    offices = []
    for o in range(num_offices):
        office = [int(attribute) if i > 0 else attribute for i, attribute in enumerate(input().split())]
        offices.append(office)
    grid = contest_space(grid, offices)
    print(f'Unallocated {unallocated_space(grid, offices)}')
    print(f'Contested {contested_space(grid)}')
    for office in offices:
        print('%s %i' % (office[0], guaranteed_space(grid, office)))


if __name__ == '__main__':
    main()
