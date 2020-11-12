def merge_tuples(tuples_list):
    i = 0
    while i < len(tuples_list):
        range_tuple = tuples_list[i]
        tuples_without_range = [x for ind, x in enumerate(tuples_list) if ind != i]
        # Check if length of list of tuples without range_tuple is zero
        i += 1 if not len(tuples_without_range) else 0
        for ind, other_range in enumerate(tuples_without_range):
            if other_range[0] <= range_tuple[0] <= other_range[1] <= range_tuple[1]:
                range_tuple = (other_range[0], range_tuple[1])
                tuples_list[i] = range_tuple
                tuples_list.remove(other_range)
                if ind < i:
                    i += 1
                i = tuples_list.index(range_tuple)
                break
            elif range_tuple[0] <= other_range[0] <= range_tuple[1] < other_range[1]:
                range_tuple = (range_tuple[0], other_range[1])
                tuples_list[i] = range_tuple
                tuples_list.remove(other_range)
                if ind < i:
                    i -= 1
                break
            elif range_tuple[0] < other_range[0] and range_tuple[1] > other_range[1]:
                tuples_list.remove(other_range)
                if ind < i:
                    i -= 1
                break
            elif range_tuple[0] > other_range[0] and range_tuple[1] < other_range[1]:
                tuples_list.remove(range_tuple)
                break
            elif ind == len(tuples_without_range) - 1:
                i += 1

    sorted_ranges = [None] * len(tuples_list)
    for range_index, range_tuple in enumerate(tuples_list):
        i = len(tuples_list) - 1
        for other_range in [x for i, x in enumerate(tuples_list) if i != range_index]:
            if range_tuple[1] < other_range[0]:
                i -= 1
        sorted_ranges[i] = range_tuple

    return sorted_ranges


def sort_by_interval_size(tuples_list):
    sorted_ranges = [None] * len(tuples_list)
    for range_index, range_tuple in enumerate(tuples_list):
        i = len(tuples_list) - 1
        range1 = range_tuple[1] - range_tuple[0]
        for other_range in [x for i, x in enumerate(tuples_list) if i != range_index]:
            range2 = other_range[1] - other_range[0]
            if (range1 < range2
                    or range1 == range2
                    and range_tuple[0] < other_range[0]):
                i -= 1
        sorted_ranges[i] = range_tuple

    return sorted_ranges


def test_cases():
    assert merge_tuples([(-1, 2), (3, 4)]) == [(-1, 2), (3, 4)]
    assert merge_tuples([(3, 4), (-1, 2)]) == [(-1, 2), (3, 4)]
    assert merge_tuples([(-1, 3), (3, 4)]) == [(-1, 4)]
    assert merge_tuples([(-1, 7), (3, 10)]) == [(-1, 10)]
    assert merge_tuples([(3, 10), (-1, 7)]) == [(-1, 10)]
    assert merge_tuples([(-1, 3), (-1, 6)]) == [(-1, 6)]
    assert merge_tuples([(-3, 6), (-5, 6)]) == [(-5, 6)]
    assert merge_tuples([(-6, 0), (-7, -1)]) == [(-7, 0)]
    assert merge_tuples([(-1, 1), (-2, 2), (-3, 3)]) == [(-3, 3)]
    assert merge_tuples([(0, 100), (1, 99), (2, 98)]) == [(0, 100)]
    assert merge_tuples([(2, 98), (1, 99), (0, 100)]) == [(0, 100)]
    assert merge_tuples([(0, 1), (0, 1), (0, 1)]) == [(0, 1)]

    assert sort_by_interval_size([(0, 2), (3, 5), (6, 8), (7, 8), (10, 11)]) == [
                                                                                (7, 8), (10, 11),
                                                                                (0, 2), (3, 5),
                                                                                (6, 8)]


def main():
    num_lines = int(input())
    tuples_list = []
    while 0 < num_lines:
        range_tuple = input().split()
        temp_tuple = (int(range_tuple[0]), int(range_tuple[1]))
        tuples_list.append(temp_tuple)
        num_lines -= 1
    merged_ranges = merge_tuples(tuples_list)
    sorted_ranges = sort_by_interval_size(merged_ranges)
    test_cases()
    print(merged_ranges)
    print(sorted_ranges)


if __name__ == "__main__":
    main()
