from typing_extensions import SupportsIndex


def binary_search(sorted_list: list, value) -> SupportsIndex:
    if sorted_list == []:
        return -1
    max_pointer = len(sorted_list)
    min_pointer = 0
    curr_index: SupportsIndex = max_pointer // 2
    while sorted_list[curr_index] != value:
        if sorted_list[curr_index] > value:
            max_pointer = curr_index
        elif sorted_list[curr_index] < value:
            min_pointer = curr_index + 1
        if (max_pointer - min_pointer) == 0:
            return -1
        curr_index: SupportsIndex = min_pointer + \
            ((max_pointer - min_pointer) // 2)
    return curr_index
